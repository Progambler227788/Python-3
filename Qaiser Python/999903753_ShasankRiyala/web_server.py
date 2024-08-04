# Imports Libraries to be used for handling server side requests
# These are all basic standard libraries of Python. No need to install explicitly
from http.server import SimpleHTTPRequestHandler 
from socketserver import ThreadingMixIn, TCPServer
from server_module import log_server_details
import time
start_time = 0
end_time = 0

class ThreadedHTTPHandler(ThreadingMixIn, SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Display/log request and header lines for debugging
        print(f"Request: {format % args}")
        # Log relevant server details
        log_server_details(self.request)

    def do_GET(self):
        global start_time, end_time  # Declare as global
        # Record the start time
        start_time = time.time()

        # Redirect directory requests to a default file (e.g., index.html)
        if self.path.endswith('/'):
            self.path += 'index.html'

        # Call the parent class method to handle the actual GET request
        super().do_GET()

        # Record the end time after sending the response
        end_time = time.time()

        # Calculate and display RTT
        rtt = end_time - start_time
        print(f"Round Trip Time (RTT): {rtt} seconds")

# Choose any available port like 8080
port = 8080
server = TCPServer(('localhost', port), ThreadedHTTPHandler)

# Starting the server with port 8080
print(f"Server running on port {port}")
server.serve_forever()
