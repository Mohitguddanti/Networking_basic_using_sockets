import socket

HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "[DISCONNECT!]"
SERVER = "192.168.137.1"

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((SERVER,PORT))

def send():
	fhand = open('data.dat')
	for message in fhand:
		mysocket.send(message.encode('utf-8'))

	mysocket.send(DISCONNECT_MESSAGE.encode('utf-8'))	

send()		