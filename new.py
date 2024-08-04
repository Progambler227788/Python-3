import RPi.GPIO as GPIO
import time
from websockets import serve
import asyncio

# Wheel DC Motor PINS
ENABLE_A = 14  # Control Speed of Left Motors
INPUT_1 = 15    # Left motors
INPUT_2 = 13    # Left motors
INPUT_3 = 2     # Right motors
INPUT_4 = 0     # Right motors
ENABLE_B = 12    # Control Speed of Right Motors

BATTERY_PIN = 0  # Battery analog pin to measure voltage

# GPIO Pin for Rover Headlights
ROVER_HEADLIGHTS = 5

# Websocket variables
ws_num = 0

# Set the Overall Rover speed
rover_speed = 220

# Set the Forward and Backward Rover speed
rover_fw_bw_speed = 135

# Set the Turning Rover speed
rover_lr_speed = 200

# Multiple coefficient to give more turning power.
turn_coefficient = 45

# Color detected
is_color_detected = False
color_detected = "NC"

# Rover Headlights
rover_headlights = 5

# Battery Voltage Measurements
battery_volt_coef = 1.98  # Coefficient ratio
cutoff_volt = 5.5  # Voltage that requires recharge
battery_volt = 7.2  # Source Battery voltage
actual_voltage = 0.0
battery_percent = 0

# Game Configuration
is_game_started = False
rover_conn_msg = "Rover Connected"
connected = ""

# WebSocket server handler
async def server_handler(websocket, path):
    global ws_num, actual_voltage, battery_percent, is_game_started, rover_conn_msg, connected, is_color_detected, color_detected

    ws_num += 1
    battery_percent = get_battery_voltage()

    connected = rover_conn_msg + "|" + str(actual_voltage) + "|" + str(battery_percent)
    await websocket.send(connected)

    print("<WSC>")  # Send to Arduino that the WebSocket connection has been established.

    try:
        async for message in websocket:
            if message == '1' or message == '4':  # 1 - Classic Mode, 2 - Planet Hop Mode, 3 - Guided Mode, 4 - Sudden Death
                is_game_started = True
                print("<GS>")
            elif message == '3':
                is_game_started = True
                print("<GM>")
            elif message == '2':
                is_game_started = True
                print("<PH>")
            elif message == 'F':
                move_forward()
            elif message == 'B':
                move_backward()
            elif message == 'L':
                move_left()
            elif message == 'R':
                move_right()
            elif message == 'S':
                stop_rover()
    finally:
        print("<GE>")  # Send to Arduino that the game is ended.
        stop_rover()
        is_game_started = False


def setup():
    global ws_num

    GPIO.setmode(GPIO.BOARD)

    # DC motor pins assignment
    GPIO.setup(ENABLE_A, GPIO.OUT)
    GPIO.setup(ENABLE_B, GPIO.OUT)
    GPIO.setup(INPUT_1, GPIO.OUT)
    GPIO.setup(INPUT_2, GPIO.OUT)
    GPIO.setup(INPUT_3, GPIO.OUT)
    GPIO.setup(INPUT_4, GPIO.OUT)

    # GPIO Pin for Rover Headlights
    GPIO.setup(ROVER_HEADLIGHTS, GPIO.OUT)

    # Retry connection until timeout
    count = 0
    while count < 17 and not is_wifi_connected():
        time.sleep(0.5)
        count += 1

    if not is_wifi_connected():
        while True:
            pass

    # Let Arduino know that Wifi connection has been established.
    print("<C>")

    # Start the WebSocket server
    asyncio.get_event_loop().run_until_complete(serve(server_handler, '0.0.0.0', 5045))
    asyncio.get_event_loop().run_forever()


def loop():
    pass


def is_wifi_connected():
    try:
        response = os.system("ping -c 1 google.com")
        return response == 0
    except Exception as e:
        print("Error checking WiFi connection:", str(e))
        return False


def move_forward():
    if is_game_started:
        GPIO.output(INPUT_1, GPIO.HIGH)
        GPIO.output(INPUT_2, GPIO.LOW)
        GPIO.output(INPUT_3, GPIO.HIGH)
        GPIO.output(INPUT_4, GPIO.LOW)
        GPIO.output(ENABLE_A, GPIO.HIGH)
        GPIO.output(ENABLE_B, GPIO.HIGH)


def move_backward():
    if is_game_started:
        GPIO.output(INPUT_1, GPIO.LOW)
        GPIO.output(INPUT_2, GPIO.HIGH)
        GPIO.output(INPUT_3, GPIO.LOW)
        GPIO.output(INPUT_4, GPIO.HIGH)
        GPIO.output(ENABLE_A, GPIO.HIGH)
        GPIO.output(ENABLE_B, GPIO.HIGH)


def move_right():
    if is_game_started:
        GPIO.output(INPUT_1, GPIO.LOW)
        GPIO.output(INPUT_2, GPIO.HIGH)
        GPIO.output(INPUT_3, GPIO.HIGH)
        GPIO.output(INPUT_4, GPIO.LOW)
        GPIO.output(ENABLE_A, GPIO.HIGH)
        GPIO.output(ENABLE_B, GPIO.HIGH)


def move_left():
    if is_game_started:
        GPIO.output(INPUT_1, GPIO.HIGH)
        GPIO.output(INPUT_2, GPIO.LOW)
        GPIO.output(INPUT_3, GPIO.LOW)
        GPIO.output(INPUT_4, GPIO.HIGH)
        GPIO.output(ENABLE_A, GPIO.HIGH)
        GPIO.output(ENABLE_B, GPIO.HIGH)


def stop_rover():
    if is_game_started:
        GPIO.output(INPUT_1, GPIO.LOW)
        GPIO.output(INPUT_2, GPIO.LOW)
        GPIO.output(INPUT_3, GPIO.LOW)
        GPIO.output(INPUT_4, GPIO.LOW)
        GPIO.output(ENABLE_A, GPIO.LOW)
        GPIO.output(ENABLE_B, GPIO.LOW)


def get_battery_voltage():
    global actual_voltage, battery_percent

    analog_voltage_value = 0.0

    for i in range(10):
        analog_voltage_value += GPIO.input(BATTERY_PIN)
        time.sleep(0.005)

    analog_voltage_value /= 10.0  # Get the average voltage measurement to be accurate.
    actual_voltage = (analog_voltage_value / 1024.0) * 5 * battery_volt_coef

    battery_percent = get_voltage_in_percentage(actual_voltage)  # Get the percentage value.

    # Ensure the percent is between 0-100%
    if battery_percent >= 100:
        battery_percent = 100
    elif battery_percent <= 0:
        battery_percent = 0

    return battery_percent


def get_voltage_in_percentage(actual_voltage):
    percent_diff = ((actual_voltage - cutoff_volt) / (battery_volt - cutoff_volt)) * 100
    return percent_diff


if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        GPIO.cleanup()
