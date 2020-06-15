import socket


# client
c = socket.socket()

# connect to the server
c.connect(('localhost', 9999))

# send name
name = input("What is your name?")
c.send(bytes(name, 'utf-8'))
# check the response from server. 1024 buffer size

server_res = c.recv(1024).decode()

print("Response from server: ", server_res)