# Imports Libraries to be used for handling server side requests
# These are all basic standard libraries of Python. No need to install explicitly
import socket
from client_module import log_client_details
import time

def main():
    # Input your server IP, port, and requested file to see details about file
    # input localhost for testing on the local machine
    server_ip = input("Enter server IP (default is localhost): ") or 'localhost'
    # input 8080 for testing
    port = int(input("Enter server port (default is 8080): ") or 8080)
    # If your code file and requested file are in the same folder, then just enter the file name like index.html
    # Server code expects the file to be in the current working directory
    requested_file = input("Enter requested file name (with path): ")

    # Create a socket and connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # make connection using ip and port
        s.connect((server_ip, port))
        # Log relevant client details
      #  log_client_details(s)

        # Record the start time
        start_time = time.time()

        # Send a simple HTTP GET request
        request = f"GET {requested_file} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
        s.sendall(request.encode())

        # Receive and display the response
        response = s.recv(1024).decode()
        print(response)

        # Record the end time
        end_time = time.time()

        # Receive the rest of the response and save it locally
        with open("downloaded_file.html", "w") as file:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                file.write(data.decode())

        print("File downloaded and saved as 'downloaded_file.html'.")

        # Calculate and display RTT
        rtt = end_time - start_time
        print(f"Round Trip Time (RTT): {rtt} seconds")

# driver code
if __name__ == "__main__":
    main()
