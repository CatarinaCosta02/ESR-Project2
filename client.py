import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.0.0.10', 8000)
print(f'connecting to {server_address[0]} port {server_address[1]}')
sock.connect(server_address)

try:
    # Send data
    message = 'This is the message. It will be repeated.'
    print(f'sending "{message}"')
    sock.sendall(message.encode('utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f'received "{data.decode("utf-8")}"')

finally:
    print('closing socket')
    sock.close()
