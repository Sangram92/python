import socket

# object creation
s = socket.socket()
print("Socket Created")

# pass host and port as a object
s.bind(('localhost', 9999))

# no of connection allowed
s.listen(3)
print('waiting for connections')

while True:
	# c: client, addr: listening on
	c, addr = s.accept()
	name = c.recv(1024).decode()
	print("Connected with: ", addr, name)

	# send message in bytes
	c.send(bytes("Welcome to Socket Programming {}".format(name), 'utf-8'))