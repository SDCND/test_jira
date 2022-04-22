#!/usr/bin/env python 

""" 
A simple echo client 
""" 

import socket 

host = '192.168.0.223'
port = 8081 
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send(b'Hello, world')
data = s.recv(size) 
s.close() 
print('Received:', data)