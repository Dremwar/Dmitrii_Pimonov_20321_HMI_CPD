# Dremwar_HMI
Задание: Task_4 Клиент отправляет видео на PySide6 сервер, где проиходит отображение этого видео в виджете.

# Описание программы 4:
В этих двух программах сервира и клиента я реализовал отправку видео на сервер PySide6 и его воспроизведения.

# Листинг 4:
Сервер(server_mp4.py)
```Py
#Импорт библиотек
import socket
import cv2
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
import numpy as np

#Функция создания сервера и отображения подключения клиента
def show_video_in_widget(video_widget):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen()
    print("Server started, waiting for client...")

    client_socket, _ = server_socket.accept()
    print("Client connected!")

    # Отображаем видео в виджете
    while True:
        frame = receive_frame(client_socket)
        if frame is None:
            break
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width,_ = image.shape
        q_image = QImage(image.data, width, height, image.strides[0], QImage.Format_RGB888)
        pix_map = QPixmap.fromImage(q_image)
        pix_map = pix_map.scaled(video_widget.size(), Qt.AspectRatioMode.KeepAspectRatio)
        video_widget.setPixmap(pix_map)
        QApplication.processEvents()

    #Закрытие сервера
    client_socket.close()
    server_socket.close()
    print("Server closed!")

def receive_frame(client_socket):
    frame_size_data = b""
    while len(frame_size_data) < 4:
        frame_size_data += client_socket.recv(4 - len(frame_size_data))
    frame_size = int.from_bytes(frame_size_data, "big")
    if frame_size == 0:
        return None
    frame_data = b""
    while len(frame_data) < frame_size:
        frame_data += client_socket.recv(frame_size - len(frame_data))
    frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)
    return frame

#Запуск программы и всех функций
if __name__ == "__main__":
    app = QApplication([])
    video_widget = QLabel()
    video_widget.setGeometry(100, 100, 800, 500)
    video_widget.show()
    show_video_in_widget(video_widget)
    app.exec()
```
Клиент(client_mp4.py)
```Py
#Импорт библиотек
import socket
import cv2

#Функция отправки видео на сервер
def send_video(video_path, server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))

    video_capture = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_data = cv2.imencode(".jpg", frame)[1].tobytes()
        frame_size_data = len(frame_data).to_bytes(4, "big")

        client_socket.sendall(frame_size_data)
        client_socket.sendall(frame_data)

    client_socket.sendall((0).to_bytes(4, "big"))
    client_socket.close()
    print("Video sent!")

#Запуск программы и настройка пути до файла mp4
if __name__ == "__main__":
    video_path = "C:/Users/00488/OneDrive/Рабочий стол/videoplayback.mp4"  # Путь к видео файлу
    server_address = "127.0.0.1"  # IP адрес сервера
    server_port = 12345  # Порт сервера

    send_video(video_path, server_address, server_port)
```

