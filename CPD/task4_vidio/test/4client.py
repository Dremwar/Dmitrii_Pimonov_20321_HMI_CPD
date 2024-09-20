import sys
import requests
import cv2
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QImage, QPixmap

class VideoWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Upload and Display")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Upload a video")
        layout.addWidget(self.label)

        self.upload_button = QPushButton("Upload Video")
        self.upload_button.clicked.connect(self.upload_video)
        layout.addWidget(self.upload_button)

        self.video_label = QLabel()
        layout.addWidget(self.video_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def upload_video(self):
        file_path = "D:\git\Dmitrii_Pimonov_20321_HMI_CPD/videoplayback.mp4"  # Укажите путь к вашему видео
        with open(file_path, 'rb') as f:
            response = requests.post("http://127.0.0.1:5000/upload", files={'file': f})
            if response.status_code == 200:
                self.play_video(file_path)

    def play_video(self, file_path):
        cap = cv2.VideoCapture(file_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            height, width, _ = frame.shape
            q_img = QImage(frame.data, width, height, width * 3, QImage.Format_RGB888).rgbSwapped()
            self.video_label.setPixmap(QPixmap.fromImage(q_img))
            cv2.waitKey(30)  # Задержка для контроля скорости отображения

        cap.release()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoWidget()
    window.show()
    sys.exit(app.exec())
