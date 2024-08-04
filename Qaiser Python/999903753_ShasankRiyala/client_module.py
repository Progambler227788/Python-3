# client_module.py
# Printing details about host name, socket family, socket type, protocol, timeout, and peername
import socket

def log_client_details(client_socket):
    # Get relevant client details
    client_details = {
        'Host Name': socket.gethostname(),
        'Socket Family': client_socket.family,
        'Socket Type': client_socket.type,
        'Protocol': client_socket.proto,
        'Timeout': client_socket.gettimeout(),
        'Peer Name': client_socket.getpeername()
    }
    print("Client Details:", client_details)
