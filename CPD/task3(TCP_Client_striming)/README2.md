# Dremwar_HMI
Задание: TCP Client-streaming (Клиент, например, раз в 1 секунду отправляет данные на сервер), используя встроенный в Python модуль socket.

Task_3_1_server.py Task_3_1_client.py Используя encode() и decode()

Task_3_2_server.py Task_3_2_client.py Используя pickle - де/сериализация произвольных объектов.

Task_3_3_server.py Task_3_3_client.py Используя Google Protocol Buffers - де/сериализация определенных структурированных данных, а не произвольных объектов Python

# Описание программы 3.1:
В этих двух программа я реализовал клиента, который с помошью функции encode() закодирует время и отправляет его на сервер, который с помошью функции decode() раскодирует и выводит его в командную строку

# Листинг 3.1:
Сервер(server3.1)
```Py
import socket
#
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        #подключаемся
        print(f"Сервер подключился к {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            #выводим данные
            print(data.decode())
```

Клиент(client3.1)

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
    # Выводим отправленные данные
    print('Sent data:', data)
    # Ждем 1 секунду
    time.sleep(1)

```

Скриншот1(отправка данных):

![image](https://github.com/Dremwar/Dmitrii_Pimonov_20321_HMI_CPD/assets/96596871/dbebe2b3-2a51-4638-b622-803485735a21)


Скриншот2(приём данных):

![image](https://github.com/Dremwar/Dmitrii_Pimonov_20321_HMI_CPD/assets/96596871/211fe55d-0995-45c7-af87-82590e5aa166)


# Описание программы 3.2:
В этих двух программа я реализовал клиента, который с помошью функции pickle()  закодирует время и отправляет его на сервер, а потом с помошью такой-же функции но на сервере раскодировать и вывести в командную строку.

# Листинг 3.2:
Сервер(server3.2)
```Py
import socket
import pickle
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Сервер подключился к {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(pickle.loads(data))
            conn.sendall(data)
```

Клиент(client3.2)

```Py
import socket
import time
import pickle

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
    data = str(time.ctime())+' pickle'
    # Отправляем данные на сервер
    data_string = pickle.dumps(data)
    #используем функцию pickle для отправки данных
    client_socket.send(pickle.dumps(data, pickle.HIGHEST_PROTOCOL))
    print('Sent data:', data)
    # Ждем 1 секунду
    time.sleep(1)
```

Скриншот3(Отправка данных через pickle):

![image](https://github.com/Dremwar/Dmitrii_Pimonov_20321_HMI_CPD/assets/96596871/e7b594df-20e6-4d24-9949-b1c9a1ecab2b)

Скриншот4(приём данных xthtp pickle):

![image](https://github.com/Dremwar/Dmitrii_Pimonov_20321_HMI_CPD/assets/96596871/35dc3e60-fe4f-4245-8959-7fdf39415ce5)

# Описание программы 3.2:
В этих двух программа я реализовал клиента, который с помошью функции pickle()  закодирует время и отправляет его на сервер, а потом с помошью такой-же функции но на сервере раскодировать и вывести в командную строку.
    
# Листинг 3.3:
Сервер(server3.2)
```Py

```
Клиент(client3.3)
```Py
import socket
import pickle
import protolc_pb2
import time

tempev = protolc_pb2.TempEvent()
tempev.device_id = 1234
tempev.event_id = 4321
tempev.humidity = 2.6
tempev.temp_cel = 3.1415

a = tempev.SerializeToString()

sock = socket.socket()
SERVER_IP = 'localhost'
SERVER_PORT = 12345

sock.connect((SERVER_IP, SERVER_PORT))

while True:
    try:

        time.sleep(1)
        sock.send(a)
        

       # time.sleep(1)
        #sock.send(pickle.dumps(data_pick, pickle.HIGHEST_PROTOCOL))
    except KeyboardInterrupt:
        break

sock.close()
```

