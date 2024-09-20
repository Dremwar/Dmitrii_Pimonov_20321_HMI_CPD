from flask import Flask, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__)
video_file_path = 'received_video.mp4'

@app.route('/upload', methods=['POST'])
def upload_file():
    global video_file_path
    file = request.files['file']
    file.save(video_file_path)
    return "Файл загружен", 200

@app.route('/play', methods=['GET'])
def play_video():
    return send_file(video_file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
