#!/usr/bin/evn python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('104.236.139.161', 21576)
print 'connecting to %s prot %s' % server_address

sock.connect(server_address)

message = 'This is the message, I am Rabbit'

print 'sending %s' % message
sock.sendall(message)

receivedCount = 0
expectedCount = len(message)

while receivedCount < expectedCount:
	data = sock.recv(16)
	receivedCount += len(data)

sock.close()
