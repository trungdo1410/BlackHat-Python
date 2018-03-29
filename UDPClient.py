																																																																																																																																	import socket

target_host = "127.0.0.1"
target_port = 80


#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#connect the client


#send some data
client.sendto("123456789", (target_host, target_port))

#receive some data
data, addr = client.recvfrom(4096)

print data
