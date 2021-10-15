import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
print("Устанавливаем связь с сервером")
sock.connect(('10.38.165.12', 9090))

while True:
  msg = input()
  if msg=='exit':
    break
  print("Отправляем данные серверу")
  sock.send(msg.encode())

  print("Принимаем данные от сервера")
  data = sock.recv(1024)

  print("Закрываем соединение")
  sock.close()

  print(data.decode())
