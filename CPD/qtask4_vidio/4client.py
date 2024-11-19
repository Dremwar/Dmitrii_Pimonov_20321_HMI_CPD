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
