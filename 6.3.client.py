import socket
import os
import sys
import shutil

host='192.168.43.219'
port=5000
c=socket.socket()

try:
	c.connect((host,port))
except socket.error as e:
        print(str(e))

print('THIS IS A CALCULATOR')
while True:

	message = input('Method: (multiply / divide / addition / substract / log / sqrt / expo): ')
	c.send(message.encode('utf-8'))

	if message == 'exit':
		print('Thank you !')
		sys.exit()

	elif message== 'multiply' or message=='divide' or message== 'addition' or message=='substract':
		number1 = input('Enter the first number: ')
		c.send(number1.encode('utf-8'))
		number2 = input('Enter the second number: ')
		c.send(number2.encode('utf-8'))

	elif message=='log' or message=='sqrt' or message=='expo':
		number1 = input('Enter a number: ')
		c.send(number1.encode('utf-8'))

	else:
		print('WRONG / UNIDENTIFIED METHOD ')
		sys.exit()
	result = c.recv(2048)
	#total = client.decode('utf-8')
	print('Total: '+ result.decode('utf-8'))

c.close()

