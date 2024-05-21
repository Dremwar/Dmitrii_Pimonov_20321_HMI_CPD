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

    def deleteProduct(self, request, context):
        print("deleteProduct:request", request)
        id = request.value
        if str(id) in self.productMap:
            del self.productMap[str(id)]
            response = product_info_pb2.Empty()
            print("deleteProduct:response", response)
            return response
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Product not found")
            return product_info_pb2.Empty()

#Создаём GRPC сервер
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#используйте сгенерированную функцию `add_ProductInfoServicer_to_server` чтобы добавить определенный класс на сервер
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