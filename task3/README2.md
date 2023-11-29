# Dremwar_HMI
Задание: TCP Client-streaming (Клиент, например, раз в 1 секунду отправляет данные на сервер), используя встроенный в Python модуль socket.

Task_3_1_server.py Task_3_1_client.py Используя encode() и decode()

Task_3_2_server.py Task_3_2_client.py Используя pickle - де/сериализация произвольных объектов.

Task_3_3_server.py Task_3_3_client.py Используя Google Protocol Buffers - де/сериализация определенных структурированных данных, а не произвольных объектов Python

# Описание программы:
В данной программе на языке Python я с помошью методов psutil создаю Дичпечер задач, который занимается отслеживанием процессов и загруженности компьютера. Программа разделена на нескольно частей. В первой части мы импортируем интерисующие нас библиотеки. Затем мы создаём класс в котором инициализируем наши основные переменные и создаём окно tekinter для визализации диспечера задач. Потом мы заполняем наше окно текинтера кнопками для обновления, добавляем полосу прокрутки. После этого я создал отдельные вкладки на окне tekinter под названиями (Процессы, процессор, память, диски, сеть). Далее в каждое из окон я занёс информацию по процессам загружающим компьютер. В конце я создаю фуккцию замершающую процесс и функцию обновления графиков с таблицами.

# Листинг 3:
Сервер
```Py
import http.server
import socketserver

# Указываем IP адрес и порт, на котором будет запущен сервер
HOST = "127.0.0.1"
PORT = 65432

# Создаем обработчик запросов
handler = http.server.SimpleHTTPRequestHandler

# Запускаем сервер
with socketserver.TCPServer((HOST, PORT), handler) as server:
    print("Сервер запущен на", HOST, "порт", PORT)
    server.serve_forever()
```

Клиент
```Py
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

```

Скриншот1:

![Screenshot_1](https://github.com/Dremwar/Dmitrii_Pimonov_20321_HMI_CPD/assets/96596871/3bf787cd-b0a6-486b-b96e-f2f86dd22b33)

Скриншот2:

![image](https://github.com/Dremwar/Dremwar_HMI/assets/96596871/a5b530de-17ab-4135-a443-a71d269f12d1)

Скриншот3:

![image](https://github.com/Dremwar/Dremwar_HMI/assets/96596871/71874c6b-54cb-4c33-8f25-9b2ed2a8e4ff)

