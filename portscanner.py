#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target using a command line argument, by hostname or IPv4 address
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid number of arguments.")
	print("Syntax: python3 portscanner.py <ip>")

# Add a banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		# Returns an error indicator of 1 or success indicator of 0
		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open.".format(port))
		s.close()

except KeyboardInterrupt:
	print("Exiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Could not connect to IP address.")
	sys.exit()
