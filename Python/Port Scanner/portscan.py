#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = raw_input("[*] Enter The Host To Scan: ")
port = int(raw_input("[*] Enter The Port To Scan: "))

def portscanner(port):
	if sock.connect_ex((host,port)):
		print("Port %d is closed" % (port))
	else:
		print("Port %d is open" % (port))

portscanner(port)
