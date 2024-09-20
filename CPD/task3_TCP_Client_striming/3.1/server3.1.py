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