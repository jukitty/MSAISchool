import socket

in_addr = socket.gethostbyname(socket.gethostname())    #IP adress  8*4=32bit   2-34e=4G   IPv6

print(in_addr)  #IP adress 192.xxx.xxx.xxx -> 사설(praivate) IP adress(공유기 IP adress) 10.xxx.xxx.xxx