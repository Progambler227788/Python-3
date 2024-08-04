import csv
import re


class Car:
    largest_car_id_attribute = 0  # static property

    def __init__(self, car_id, car_registration_plate, car_manufacturer, car_model_type, car_sipp_code,
                 car_maximum_seat_capacity, car_width, car_length, car_max_speed, car_mpg, car_on_hire):
        self.car_id = car_id
        self.car_registration_plate = self.validate_registration_plate(car_registration_plate.upper())
        self.car_manufacturer = self.validate_manufacturers(car_manufacturer.upper())
        self.car_model_type = car_model_type
        self.car_sipp_code = self.validate_sipp_code(car_sipp_code.upper())
        self.car_maximum_seat_capacity = self.validate_max_seat_capacity(car_maximum_seat_capacity)
        self.car_width = self.validate_width(car_width)
        self.car_length = self.validate_length(car_length)
        self.car_max_speed = car_max_speed
        self.car_mpg = car_mpg
        self.car_on_hire = car_on_hire

        # Update the largest_car_id_attribute if the current car_id is larger
        Car.largest_car_id_attribute = max(Car.largest_car_id_attribute, car_id)

    # Function to make sure maximum seats are valid
    @staticmethod
    def validate_max_seat_capacity(car_maximum_seat_capacity):
        # Making sure that car_maximum_seat_capacity is between 1 and 10
        if 1 <= car_maximum_seat_capacity <= 10:
            return car_maximum_seat_capacity
        raise ValueError("Seats should be between 1 and 10")

    # Function to make sure car width is in given range
    @staticmethod
    def validate_width(car_width):
        # Making sure that car_width is between 1000 and 2500
        if 100 <= car_width <= 2500:
            return car_width
        raise ValueError("Width should be between 1000 and 2500")

    # Function to make sure length is in range that is allowed
    @staticmethod
    def validate_length(car_length):
        # Making sure that car_length is between 1000 and 10000
        if 1000 <= car_length <= 10000:
            return car_length
        raise ValueError("Length should be between 1000 and 10,000")

    # Function to make sure sipp code (Standard Interline Passenger Procedures) to indicate information about car
    @staticmethod
    def validate_sipp_code(car_sipp_code):
        # Making a Regular expression for SIPP code validation
        sipp_re_expression = r"^[CDEFGHIJOPRSU][BCDFKLPQTVW][ABCDNM][CDEHINQRVZ]$"

        # Checking or Validating if the provided SIPP code matches the plate_re_expression
        if re.match(sipp_re_expression, car_sipp_code):
            return car_sipp_code
        raise ValueError("Invalid SIPP Code\nRules are given below :::\n" +
                         "Only 4 English Alphabets are allowed either upper case or lower case\n" +
                         "First letter from (CDEFGHIJOPRSU)\n" +
                         "Second letter from (BCDFKLPQTVW)\n" +
                         "Third letter from (ABCDNM)\n" +
                         "Fourth letter from (CDEHINQRVZ)\n")

    # Function to make sure that is car built by only below given list containing manufacturers
    @staticmethod
    def validate_manufacturers(car_manufacturer):
        # Valid Manufacturers that can make cars
        valid_manufacturers = ["CHEVROLET", "CHRYSLER", "FORD", "HONDA", "ISUZU", "TOYOTA"]
        if car_manufacturer in valid_manufacturers:
            return car_manufacturer
        raise ValueError(f"Invalid name of Manufacturer : ${car_manufacturer}")

    # Function to validate registration plate
    @staticmethod
    def validate_registration_plate(car_registration_plate):
        # Making a Regular Expression for Registration Plate Validation
        plate_re_expression = re.compile(
            r'(^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$)|(^[A-Z][0-9]{1,3}[A-Z]{3}$)|(^[A-Z]{3}[0-9]{1,3}[A-Z]$)|'
            r'(^[0-9]{1,4}[A-Z]{1,2}$)|(^[0-9]{1,3}[A-Z]{1,3}$)|(^[A-Z]{1,2}[0-9]{1,4}$)|'
            r'(^[A-Z]{1,3}[0-9]{1,3}$)|(^[A-Z]{1,3}[0-9]{1,4}$)|(^[0-9]{3}[DX][0-9]{3}$)'
        )
        # Validating either user entered expression matched or not
        if not plate_re_expression.match(car_registration_plate):
            raise ValueError(
                "Invalid registration plate format.\nFormat will be like AZ89 or AA9BAB or BA23 PAY or BAB33H or "
                "4321AB or 143HJK or AJK1235 ")
        return car_registration_plate

    # Method to convert values to their appropriate types like integer, float, boolean
    @classmethod
    def from_csv_row(cls, line):
        if len(line) >= 11:  # Check if there are at least 11 elements in the line like id,model-type etc. are elements
            try:
                # Convert elements of a file to correct types
                car_id = int(line[0])
                car_maximum_seat_capacity = int(line[5])
                car_width = int(line[6])
                car_length = int(line[7])
                car_max_speed = float(line[8])
                car_mpg = float(line[9])
                car_on_hire = line[10].lower() == 'true'  # Convert 'True' or 'False' to boolean

                return cls(car_id, line[1], line[2], line[3], line[4], car_maximum_seat_capacity,
                           car_width, car_length, car_max_speed, car_mpg, car_on_hire)
            except ValueError as e:
                print(f"Error converting values in line {line}: {e}")
                return cls(0, "", "", "", "", 0, 0, 0, 0, 0, False)  # Return a default instance having values zero
        else:
            print(f"Error: Insufficient elements in the line {line}. Skipping.")
            return cls(0, "", "", "", "", 0, 0, 0, 0, 0, False)  # Return a default instance having values zero


class CarRegistry:
    def __init__(self):
        self.cars = []
        self.used_registration_plates = set()  # To keep track of used plates, to ensure uniqueness
        self.load_data_from_file()

    def load_data_from_file(self):
        try:
            with open("C:\\Temp\\CarRegistry.dat", mode='r') as file:
                reader = csv.reader(file)
                self.cars.clear()
                self.used_registration_plates.clear()
                for line in reader:
                    car = Car.from_csv_row(line)
                    self.cars.append(car)
                    self.used_registration_plates.add(car.car_registration_plate)
        except FileNotFoundError:
            print("Sorry!!! File not found. Starting with an empty registry.")

    def save_data_to_file(self):
        with open("C:\\Temp\\CarRegistry.dat", mode='w', newline='') as file:
            writer = csv.writer(file)
            for car in self.cars:
                writer.writerow([car.car_id, car.car_registration_plate, car.car_manufacturer, car.car_model_type,
                                 car.car_sipp_code, car.car_maximum_seat_capacity, car.car_width, car.car_length,
                                 car.car_max_speed,
                                 car.car_mpg, car.car_on_hire])

    def unique_number_plate(self, car_registration_plate):
        if car_registration_plate in self.used_registration_plates:
            raise ValueError("Registration Plate Already Exists. Car can't be added to same Registration Number\n")
        return car_registration_plate

    def add_car(self, new_car):
        new_car.car_id = self.generate_unique_id()
        self.cars.append(new_car)
        self.used_registration_plates.add(new_car.car_registration_plate)

        with open("C:\\Temp\\CarRegistry.dat", "a") as myfile:
            writer = csv.writer(myfile, lineterminator='\n')
            writer.writerow(
                [new_car.car_id, new_car.car_registration_plate, new_car.car_manufacturer, new_car.car_model_type,
                 new_car.car_sipp_code, new_car.car_maximum_seat_capacity, new_car.car_width, new_car.car_length,
                 new_car.car_max_speed,
                 new_car.car_mpg, new_car.car_on_hire])
        print("Car added successfully to Car Registry !")

    def delete_car(self, delete_car):
        if delete_car in self.cars:
            id_car = delete_car.car_id
            self.cars.remove(delete_car)
            print(f"Car deleted successfully of ID:{id_car}")
            self.save_data_to_file()
        else:
            print("Sorry!!! Invalid position number. Car can not be deleted. Please enter correct position")

    def find_car(self, ucar_id):
        for index, car in enumerate(self.cars):
            if car.car_id == ucar_id:
                return index
        return None

    def hire_out_car_id(self, car_id):
        hiring_car_index = self.find_car(car_id)
        if hiring_car_index is None:
            return f"Sorry, the car with an ID of {car_id} is not in the Car Registry!"
        if self.cars[hiring_car_index].car_on_hire:
            return (f"Sorry, the car registered as {self.cars[hiring_car_index].car_registration_plate} and with ID: "
                    f"{car_id} is already away out on hire")
        self.cars[hiring_car_index].car_on_hire = True
        self.save_data_to_file()
        return f"The car with an ID of {car_id} is now hired!"

    def return_car_to_garage_id(self, car_id):
        return_car_index = self.find_car(car_id)
        if return_car_index is None:
            return f"Sorry, the car with an ID of {car_id} is not in the Car Registry!"
        if not self.cars[return_car_index].car_on_hire:
            return (f"Sorry, the car registered as {self.cars[return_car_index].car_registration_plate} and with ID: " +
                    f"{car_id} is already returned in garage")
        self.cars[return_car_index].car_on_hire = False
        self.save_data_to_file()
        return f"The car with an ID of {car_id} is now returned to garage!"

    def hire_out_car_position(self, position):
        if 1 <= position <= len(self.cars):
            car = self.cars[position - 1]
            if not car.car_on_hire:
                car.car_on_hire = True
                print("Car hired out successfully!")
                self.save_data_to_file()
            else:
                print("Car is already on hire.")
        else:
            print("Sorry!!! Invalid position number. Cannot hire out the car.")

    def return_car_to_garage_position(self, position):
        if 1 <= position <= len(self.cars):
            car = self.cars[position - 1]
            if car.car_on_hire:
                car.car_on_hire = False
                print("Car returned to the garage successfully!")
                self.save_data_to_file()
            else:
                print("Car is already in the garage.")
        else:
            print("Sorry!!! Invalid position number. Cannot return the car to the garage.")

    @staticmethod
    def update_car_registry():
        # Default data
        default_data = [
            "1,BD61 SLU,HONDA,CR-V,SFDR,5,1780,4510,130.0,39.0,True",
            "2,CA51 MBE,CHEVROLET,CORVETTE,JTAV,2,1877,1234,194.0,24.0,True",
            "3,PC14 RSN,FORD,F-150,PQBD,5,2121,5890,155.0,20.0,True",
            "4,MB19 ORE,HONDA,ACCORD,FDAR,5,1849,4933,125.0,47.3,False",
            "5,BD68 NAP,HONDA,ACCORD,FDAV,5,1849,4933,171.0,37.7,False",
            "6,LY51 BED,Isuzu,NQR,OKAD,3,2065,5220,114.0,11.9,True",
            "7,LJ08 NOD,HONDA,CIVIC,SDAR,5,1877,4648,125.0,31.0,True",
            "9,GK63 SLE,FORD,ESCAPE,SDMR,5,1806,4457,209.0,23.0,True",
            "10,GW66 EPY,FORD,TAURUS,FCAR,5,1935,5154,143.0,20.0,False",
            "11,YE02 FOU,TOYOTA,CELICA,IDAR,5,1778,2700,140.0,30.0,False",
            "12,YN65 RTY,CHRYSLER,CHEROKEE,PFBD,5,1900,4730,125.5,36.0,True",
            "13,WP64 WIN,CHEVROLET,SPARK,ECMR,5,1495,3495,89.0,33.0,False",
            "14,RG69 KSD,CHEVROLET,CORVETTE,JTAV,2,1877,1234,194.0,24.0,True",
            "15,HR11 OZE,FORD,F-150,PPBD,5,2121,5890,155.0,20.0,False"
        ]

        # Clear existing data and write default data to the file
        with open("C:\\Temp\\CarRegistry.dat", "w") as file:
            for line in default_data:
                file.write(line + '\n')

        print("Car registry updated successfully!\n\n")

    def generate_unique_id(self):
        if not self.cars:
            return 1
        else:
            return max(car.car_id for car in self.cars) + 1


class UI:
    def __init__(self, car_registry):
        self.my_car_registry = car_registry

    @staticmethod
    def display_header():
        # Write the header line to the console
        print("{:<10} {:<5} {:<15} {:<15} {:<15} {:<10} {:<5} {:<5} {:<5} {:<7} {:<7} {:<5}".format(
            "Position", "ID", "Reg Plate", "Manufacturer", "Model/Type", "SIPP", "Seats", "Width", "Length",
            "Max-Speed", "MPG", "On Hire"
        ))
        print("=" * 122)

    def display_items(self):
        self.my_car_registry.load_data_from_file()
        # Write the contents of the Cars Collection to the console
        i = 1
        for car in self.my_car_registry.cars:
            print("{:<10} {:<5} {:<15} {:<15} {:<15} {:<10} {:<5} {:<5} {:<5} {:<10} {:<10} {:<5}".format(
                i, car.car_id, car.car_registration_plate, car.car_manufacturer, car.car_model_type,
                car.car_sipp_code, car.car_maximum_seat_capacity, car.car_width, car.car_length, car.car_max_speed,
                car.car_mpg, car.car_on_hire
            ))
            i += 1

    @staticmethod
    def display_menu():
        # Write the menu options to the console
        print("\nOptions:")
        print("  a. Add Car")
        print("  d. Delete Car")
        print("  h. Hire Out Car")
        print("  r. Return Car to Garage")
        print("  u. Update Car Registry")
        print("  x. Exit Program")

    def add_car(self):
        try:
            try:
                car_registration_plate = input("Enter registration plate: ").upper()
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return

            car_registration_plate = Car.validate_registration_plate(car_registration_plate)
            car_registration_plate = self.my_car_registry.unique_number_plate(car_registration_plate)
            try:
                car_manufacturer = input("Enter car_manufacturer: ").upper()
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return

            car_manufacturer = Car.validate_manufacturers(car_manufacturer)

            try:
                car_model_type = input("Enter model/type: ").upper()
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return

            try:
                car_sipp_code = input("Enter SIPP code: ").upper()
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return

            car_sipp_code = Car.validate_sipp_code(car_sipp_code)

            try:
                car_maximum_seat_capacity = int(input("Enter max seat capacity: "))
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return

            car_maximum_seat_capacity = Car.validate_max_seat_capacity(car_maximum_seat_capacity)

            try:
                car_width = int(input("Enter car_width: "))
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return
            car_width = Car.validate_width(car_width)
            try:
                car_length = int(input("Enter car_length: "))
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return

            car_length = Car.validate_length(car_length)
            try:
                car_max_speed = float(input("Enter max speed: "))
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return

            try:
                car_mpg = float(input("Enter MPG: "))
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return
            try:
                car_on_hire = input("Is the car on hire? (True/False): ").lower() == 'true'
            except KeyboardInterrupt:
                print("Operation Halt by User by terminating program process")
                return

            new_car = Car(0, car_registration_plate, car_manufacturer, car_model_type, car_sipp_code,
                          car_maximum_seat_capacity, car_width, car_length, car_max_speed, car_mpg, car_on_hire)
            self.my_car_registry.add_car(new_car)

        except ValueError as p:
            print(f"Error: {p}")
            pass

    # Method to call delete car
    def delete_car(self):
        if len(self.my_car_registry.cars) == 0:
            print("No cars")
            return
        try:
            print("You have two Options Below:\nj. Delete Car by ID\n")
            print("t. Delete Car by Position\n")
            option = input("Enter choice: ").lower()
            if option == 't':
                position = int(input("Enter the position number of the car to delete: "))
                self.my_car_registry.delete_car(self.my_car_registry.cars[position - 1])
            elif option == 'j':
                car_id = int(input("Enter the ID of the car to delete: "))
                index = self.my_car_registry.find_car(car_id)
                if index is not None:
                    self.my_car_registry.delete_car(self.my_car_registry.cars[index])
                else:
                    print(f"Sorry, the car with an ID of {id} is not in the Car Registry!")
        except ValueError:
            print("Error: Try to enter only number")
            pass

    # Method to call hire out car
    def hire_out_car_position(self):
        try:
            print("You have two Options Below:\nj. Hire Car by ID\n")
            print("t. Hire Car by Position\n")
            option = input("Enter choice: ").lower()
            if option == 't':
                position = int(input("Enter the position number of the car to hire out: "))
                self.my_car_registry.hire_out_car_position(position)
            elif option == 'j':
                car_id = int(input("Enter the ID of the car to hire out: "))
                print(self.my_car_registry.hire_out_car_id(car_id))
            else:
                print("Only j/J or t/T are options. Invalid option")
        except ValueError:
            print("Error: Try to enter only number")
            pass

    # Method to call return car to garage
    def return_car_to_garage_position(self):
        try:
            print("You have two Options Below:\nj. Return Car by ID\n")
            print("t. Return Car by Position\n")
            option = input("Enter choice: ").lower()
            if option == 't':
                position = int(input("Enter the position number of the car to return: "))
                self.my_car_registry.return_car_to_garage_position(position)
            elif option == 'j':
                car_id = int(input("Enter the ID of the car to return: "))
                print(self.my_car_registry.return_car_to_garage_id(car_id))
            else:
                print("Only j/J or t/T are options. Invalid option")
        except ValueError:
            print("Error: Try to enter only number")
            pass

    # Method to update car registry
    def update_car_registry(self):
        self.my_car_registry.update_car_registry()

    # Exit Program function
    def exit_program(self):
        confirm_exit = input("Are you sure you want to exit? (y/n): ").lower()
        if confirm_exit == 'y':
            exit()
        elif confirm_exit == 'n':
            self.display_items()
            self.display_menu()
            user_input = input("Enter option: ")
            self.process_option(user_input)
        else:
            print("Invalid option. Exiting program.")
            exit()

    # Function to take decision on basis of entered option
    def process_option(self, option):
        while option.lower() != 'x':
            if option.lower() == 'a':
                self.add_car()
            elif option.lower() == 'd':
                self.delete_car()
            elif option.lower() == 'h':
                self.hire_out_car_position()
            elif option.lower() == 'r':
                self.return_car_to_garage_position()
            elif option.lower() == 'u':
                self.update_car_registry()
            else:
                print("Invalid option. Please try again.")

            # Display header, updated state and menu
            self.display_header()
            self.display_items()
            self.display_menu()

            # Get the next user input
            option = input("Enter option: ").lower()

        # If 'x' is entered, exit the program
        self.exit_program()


def main():
    car_registry = CarRegistry()
    ui = UI(car_registry)

    # Display initial state
    ui.display_header()
    ui.display_items()
    ui.display_menu()

    # Process user input
    user_input = input("Enter option: ").lower()
    ui.process_option(user_input)


# Call Main function to load functionality
if __name__ == "__main__":
    main()
