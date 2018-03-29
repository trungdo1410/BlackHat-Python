import socket

target_host = "www.phimmoi.net"
target_port = 80

#creat a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print (response)