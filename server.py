import socket

print("Запуск сервера")

def listening():
	sock = socket.socket()
	sock.bind(('', 9090))
	print("Прослушивание порта")
	sock.listen(0)
	print("Подключение клиента")
	conn, addr = sock.accept()
	print("Соединение установлено", addr)
	re = False
	msg = ''

print("Начинаем приём данных от клиента")
while True:
	data = conn.recv(1024)
	msg = data.decode()
	print(msg)
	if msg == 'exit':
		ret = True
		break
	if not data:
		break
	conn.send(data)
	print("Соединение разорвано ", addr)
	conn.close()
	return ret

ret = False
while not ret:
	ret = listening()

print("Клиент отключён")

conn.close()
