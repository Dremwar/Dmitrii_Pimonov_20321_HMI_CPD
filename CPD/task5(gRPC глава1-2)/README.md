# Dremwar_CPD
Задание:Глава 1,2
Разобрать пример Python с GitHub.
В github пример Python. С добавленным сервисом и полями, которые используются.

# Описание программы:
В данной программе на языке Python я реализовал сервер и клиент gRPC которые передают,получают и воспроизводят информацию .

# Листинг:

Сервер gRPC
```Py

#Импортируем библиотеки
from concurrent import futures
import uuid
import grpc
import time

#Загрузка сгенерированныъ файлов
import product_info_pb2
import product_info_pb2_grpc

class ProductInfoServicer(product_info_pb2_grpc.ProductInfoServicer):
    def __init__(self):
        self.productMap = {}
    #Функция Получения данных
    def addProduct(self, request, context):
        id = uuid.uuid1()
        request.id = str(id)
        print("addProduct:request", request)
        self.productMap[str(id)] = request
        response = product_info_pb2.ProductID(value = str(id))

        print("addProduct:response", response)
        return response

    #Функция отправки данных
    def getProduct(self, request, context):
        print("getProduct:request", request)
        id = request.value
        response = self.productMap[str(id)]
        print("getProduct:response", response)
        return response

#Создаём GRPC сервер
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#используйте сгенерированную функцию `add_ProductInfoServicer_to_serve  r` чтобы добавить определенный класс на сервер
product_info_pb2_grpc.add_ProductInfoServicer_to_server(ProductInfoServicer(), server)

# Открываем порт 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

#поскольку server.start() не будет блокироваться, добавим  цикл для поддержания его активности

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

```
Клиент gRPC
```Py

#Импортируем библиотеки
import grpc

#Загрузка сгенерированныъ файлов
import product_info_pb2
import product_info_pb2_grpc

#Функция отправки сообщений от клиента
def run():
    # Откроем gRPC канал
    channel = grpc.insecure_channel('localhost:50051')
    # Создание Клиента
    stub = product_info_pb2_grpc.ProductInfoStub(channel)

    #Название и описание продукта
    response = stub.addProduct(product_info_pb2.Product(name = "Apple iPhone 11", description = "Meet Apple iPhone 11. All-new dual-camera system with Ultra Wide and Night mode.", price = 699.0 ))
    print("add product: response", response)
    productInfo = stub.getProduct(product_info_pb2.ProductID(value = response.value))
    print("get product: response", productInfo)

run()

```

Скриншот1:

![image](https://github.com/Dremwar/Dmitrii_Pimonov_20321_HMI_CPD/assets/96596871/04e618c7-d820-4a9b-9493-3eb96bcfd2e0)

Скриншот2:

![image](https://github.com/Dremwar/Dmitrii_Pimonov_20321_HMI_CPD/assets/96596871/71da8e67-f28b-451d-8712-c9cf973af8cb)

Скриншот3:



