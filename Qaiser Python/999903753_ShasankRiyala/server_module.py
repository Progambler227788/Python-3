# server_module.py
# Printing details about host name, socket family, socket type, protocol, timeout, and peername

def log_server_details(request):
    # N/A means to be not available
    server_details = {
        'Host Name': request.getsockname()[0] if len(request.getsockname()) > 0 else 'N/A',
        'Socket Family': request.getsockname()[0] if len(request.getsockname()) > 1 else 'N/A',
        'Socket Type': request.getsockname()[0] if len(request.getsockname()) > 2 else 'N/A',
        'Protocol': request.getsockname()[2] if len(request.getsockname()) > 2 else 'N/A',
        'Timeout': request.timeout,
        'Peer Name': request.getpeername(),
    }

    print("Connection Details:")
    for key, value in server_details.items():
        print(f"{key}: {value}")
