#!/usr/bin/env python

"""
A simple echo client
"""
import struct
import socket
#electrode_data = [0.0, 0.0, 0.2, 0.2, -0.01, 0.0, 0.0, 0.0]
# First encode the number of data items, then the actual items
#data = struct.pack("!I" + "d" * len(electrode_data), len(electrode_data), *electrode_data)
#print(data)

# Pull the number of encoded items (Note a tuple is returned!)
#elen = struct.unpack_from("!I", data)[0]
# Now pull the array of items
#e2 = struct.unpack_from("!" + "d" * elen, data, 4)
#print(e2)

values = (0.0, 0.0, 0.2, -0.01, 0.02, 0.0, 0.0, 0.0)

import struct
import socket
import time
host = '68.180.86.216'
port = 55001
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

#values = (0.0, 0.0, x, y, z, 0.0, 0.0, 0.0)
values = (0.0, 0.0, 0.2, -0.01, 0.2, 0.0, 0.0, 0.0)
packer = struct.Struct('f f f f f f f f')
packed_data = packer.pack(*values)
s.send(packed_data)
time.sleep(2)

#values2 = (0.0, 0.0, 0.0, -0.04, 0.2, 0.0, 0.0, 0.0)
#packer2 = struct.Struct('f f f f f f f f')
#packed_data2 = packer2.pack(*values2)
#s.send(packed_data2)
#time.sleep(2)

#values3 = (0.0, 0.0, -0.02, -0.01, 0.2, 0.0, 0.0, 0.0)
#packer3 = struct.Struct('f f f f f f f f')
#packed_data3 = packer3.pack(*values3)
#s.send(packed_data3)
#time.sleep(2)

values4 = (0.0, 0.0, -0.05, -0.1, 0.2, 0.0, 0.0, 0.0)
packer4 = struct.Struct('f f f f f f f f')
packed_data4 = packer4.pack(*values4)
s.send(packed_data4)



#s.send(b'Hello, world')
data = s.recv(size)
s.close()
print ('Disconnected')