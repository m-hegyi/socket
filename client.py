import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('www.google.com', 80))

print('sending...')

response = client.recv(4096)

print(response)