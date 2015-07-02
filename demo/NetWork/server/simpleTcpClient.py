#!/usr/bin/evn python

import socket
import sys

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

BUFSIZE = 1024
server_address = ('104.236.139.161', 21576)
print 'connecting to %s prot %s' % server_address

tcpCliSock.connect(server_address)

while True:
	data = raw_input('> ')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZE)
	if not data:
		break
	print data
tcpCliSock.close()
