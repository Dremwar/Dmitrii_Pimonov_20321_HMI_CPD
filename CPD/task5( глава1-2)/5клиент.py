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
    dell=stub.add_ProductInfoServicer_to_server(ProductInfoServicer(), server)
    print("delete product: response",dell)

run()