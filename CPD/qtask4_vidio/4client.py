import sys# Импортируем библиотеки
import video_pb2
from PySide6.QtCore import QFile
from PySide6.QtNetwork import QTcpSocket
from PySide6.QtWidgets import QApplication
import struct

class VideoClient:
    def __init__(self, server_ip='127.0.0.1', server_port=12345):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = QTcpSocket()
        self.client_socket.connected.connect(self.on_connected)
        self.client_socket.connectToHost(self.server_ip, self.server_port)

    def on_connected(self):#Функция подключение клиента к серверу
        print(f"Подключено к серверу {self.server_ip}:{self.server_port}")
        self.send_video('D:\git\Dmitrii_Pimonov_20321_HMI_CPD\CPD\qtask4_vidio\qvideoplayback.mp4')  # Отправляем видео, как только подключились



    def send_video(self, filename):#Функция отправки видио
        with open(filename, 'rb') as f:
            video_data = f.read()

        chunk_size = 1024  # Размер чанка
        total_size = len(video_data)
        print(f"Начинаю отправку видео, размер файла: {total_size} байт")

        for i in range(0, total_size, chunk_size):
            chunk = video_data[i:i + chunk_size]
            # Создание сообщения Protobuf
            video_message = video_pb2.VideoData()
            video_message.video_chunk = chunk
            video_message.is_end = (i + chunk_size >= total_size)  # Устанавливаем флаг окончания

            # Сериализация данных
            serialized_message = video_message.SerializeToString()
            message_length = len(serialized_message)

            # Отправляем длину сообщения (4 байта) + само сообщение
            self.client_socket.write(struct.pack(">I", message_length))  # 4 байта длины
            self.client_socket.write(serialized_message)
            self.client_socket.flush()

        print("Видео отправлено")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Создаем объект приложения
    client = VideoClient()
    app.exec()  # Запуск приложения PySide6
