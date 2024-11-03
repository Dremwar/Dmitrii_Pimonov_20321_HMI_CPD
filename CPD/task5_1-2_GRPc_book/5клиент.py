# Импортируем библиотеки
import grpc

# Загрузка сгенерированных файлов
import product_info_pb2
import product_info_pb2_grpc

# Функция отправки сообщений от клиента
def run():
    # Открытие gRPC канала
    channel = grpc.insecure_channel('localhost:50051')
    # Создание клиента
    stub = product_info_pb2_grpc.ProductInfoStub(channel)

    # Добавление продукта
    response = stub.addProduct(
        product_info_pb2.Product(
            name="Apple iPhone 11",
            description="Meet Apple iPhone 11. All-new dual-camera system with Ultra Wide and Night mode.",
            price=699.0
        )
    )
    print("add product: response", response)

    # Получение информации о продукте
    productInfo = stub.getProduct(
        product_info_pb2.ProductID(value=response.value)
    )
    print("get product: response", productInfo)

    # Удаление продукта
    delete_response = stub.deleteProduct(
        product_info_pb2.ProductID(value=response.value)
    )
    print("delete product: response", delete_response)

# Запуск клиентской функции
run()
