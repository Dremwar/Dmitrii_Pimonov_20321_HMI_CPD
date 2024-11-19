# Dremwar_HMI
Задание: Task_4 Клиент отправляет видео на PySide6 сервер, где проиходит отображение этого видео в виджете.

# Описание программы 4:
В этих двух программах сервира и клиента я реализовал отправку видео на сервер PySide6 и его воспроизведения.

# Листинг 4:
Сервер(server_mp4.py)
```Py
#Импорт библиотек
from PySide6.QtCore import QUrl #импортируем библиотеки
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtNetwork import QTcpServer, QTcpSocket
from PySide6.QtWidgets import QApplication, QMainWindow
import os


class VideoServer(QMainWindow):# класс реализует получение и воспроизведение видио
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Video Server")

        # Настройка виджета для видео
        self.video_widget = QVideoWidget()
        self.setCentralWidget(self.video_widget)

        # Настройка QMediaPlayer
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)

        # Логирование ошибок
        self.media_player.errorOccurred.connect(self.on_error)
        self.media_player.mediaStatusChanged.connect(self.on_media_status)

        # Настройка TCP-сервера
        self.tcp_server = QTcpServer(self)
        self.tcp_server.listen(port=12345)
        self.tcp_server.newConnection.connect(self.handle_new_connection)

        self.client_socket = None
        self.buffer = bytearray()

        print("Сервер запущен на порту 12345")

    def handle_new_connection(self):#функция обработки подключений
        self.client_socket = self.tcp_server.nextPendingConnection()
        self.client_socket.readyRead.connect(self.read_data)
        self.client_socket.disconnected.connect(self.client_socket.deleteLater)
        print("Клиент подключен")

    def read_data(self):#чтение данных от клиента
        while self.client_socket.bytesAvailable():
            self.buffer.extend(self.client_socket.readAll().data())

        # Если передача завершена, сохраняем данные в видеофайл
        if b'EOF' in self.buffer:
            print("Передача завершена")
            self.buffer = self.buffer.replace(b'EOF', b'')  # Удаляем маркер EOF
            video_file = "received_video.mp4"
            with open(video_file, "wb") as f:
                f.write(self.buffer)
            self.buffer.clear()
            print(f"Видео сохранено как {video_file}")

            # Проверяем размер файла
            print(f"Размер файла: {os.path.getsize(video_file)} байт")

            # Воспроизводим видео
            self.media_player.setSource(QUrl.fromLocalFile(video_file))
            self.media_player.play()

    def on_error(self, error):#функция ощибки воспроизведения
        print(f"Ошибка воспроизведения: {error}, {self.media_player.errorString()}")

    def on_media_status(self, status):#функция воспроизведения статуса
        print(f"Статус медиа: {status}")


if __name__ == "__main__":
    app = QApplication([])
    server = VideoServer()
    server.show()
    app.exec()
```
Клиент(client_mp4.py)
```Py
import sys #Импортируем библиотеки
from PySide6.QtNetwork import QTcpSocket

def send_video():#Функция отправки видио
    file_path = "D:\git\Dmitrii_Pimonov_20321_HMI_CPD\CPD\qtask4_vidio\qvideoplayback.mp4"  # Укажите здесь путь к вашему видеофайлу
    host = "localhost"
    port = 12345

    socket = QTcpSocket()
    socket.connectToHost(host, port)

    if not socket.waitForConnected(3000):
        print("Не удалось подключиться к серверу")
        return

    print("Подключено к серверу")

    # Отправка файла
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(1024):
                socket.write(chunk)
                socket.waitForBytesWritten(3000)

        # Добавляем маркер окончания передачи
        socket.write(b'EOF')
        socket.waitForBytesWritten(3000)
        print("Видео отправлено")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        socket.close()

if __name__ == "__main__":
    send_video()
```
![alt text](image.png)

