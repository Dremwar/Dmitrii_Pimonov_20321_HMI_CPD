import socket
import time

# IP-адрес и порт сервера
SERVER_IP = '127.0.0.1'
SERVER_PORT = 65432

# Создаем TCP сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем соединение с сервером
client_socket.connect((SERVER_IP, SERVER_PORT))
print('Connected to server')

while True:
    # Генерируем данные для отправки
    data = str(time.ctime())
    # Отправляем данные на сервер
    client_socket.sendall(data.encode())
    print('Sent data:', data)
    # Ждем 1 секунду
    time.sleep(1)
