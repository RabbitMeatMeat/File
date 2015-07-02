#!usr/bin/env python
#_*_ coding: utf-8 _*_

'a simple TcpServer'

__author__ = 'Rabbit.Meat'

import sys
import socket
from time import ctime

def test():
	HOST = '104.236.139.161'
	PORT = 21576
	BUFSIZE = 1024
	ADDR = (HOST, PORT)

	tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcpSerSock.bind(ADDR)
	tcpSerSock.listen(5)
	while True:
		print 'waiting for connection...'
		tcpCliSock, addr = tcpSerSock.accept()
		print '...connected from: ', addr

		while True:
			data = tcpCliSock.recv(BUFSIZE)
			if not data:
				break
			tcpCliSocket.send('[%s] %s' % (ctime(), data))

		tcpCliSock.close()
	tcpSerSock,close()
if __name__ == '__main__':
	test()

