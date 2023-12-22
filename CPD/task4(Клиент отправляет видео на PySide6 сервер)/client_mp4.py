#Импорт библиотек
import socket
import cv2

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