import socket
import sys

# Create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8080)
print('connecting to {} port {}'.format(*server_address))
client.connect(server_address)

try:

    # Send data
    message = b'Banana'
    print('sending {!r}'.format(message))
    client.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = client.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing client')
    client.close()