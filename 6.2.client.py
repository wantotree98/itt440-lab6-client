import socket

ClientSocket = socket.socket()
host='192.168.43.219'
port=8888

print('Waiting for connection')
try:
	ClientSocket.connect((host, port))
except socket.error as e:
	print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
	input = input('Say something: ')
	ClientSocket.send(str.encode(input))
	Reply = ClientSocket.recv(1024)
	print(Reply.decode('utf-8'))

ClientSocket.close()
