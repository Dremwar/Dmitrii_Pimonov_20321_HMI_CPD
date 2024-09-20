import requests
import sys

def upload_video(video_path):
    url = 'http://127.0.0.1:5000/upload'
    with open(video_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
    print(response.text)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Использование: python client.py <path_to_video>")
        sys.exit(1)

    video_path = sys.argv[1]
    upload_video(video_path)
