#!usr/bin/env python
#_*_ coding: utf-8 _*_

'a simple TcpServer'

__author__ = 'Rabbit.Meat'

import sys
import socket
from time import ctime

def test():
	HOST = 'localhost'
	PORT = 21576
	BUFSIZE = 1024
	ADDR = (HOST, PORT)

	tcpSerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcpSerSocket.bind(ADDR)
	tcpSerSocket.listen(5)
	while True:
		print 'waiting for connection...'
		tcpCliSocket, addr = tcpSerSocket.accept()
		print '...connected from: ', addr

		while True:
			data = tcpCliSocket.recv(BUFSIZE)
			if not data:
				break
			tcpCliSocket.send('[%s] %s' % (ctime(), data))

		tcpCliSocket.close()
	tcpSerSocket,close()
if __name__ == '__main__':
	test()

