from google.protobuf import wrappers_pb2 # Импорт модулей для работы с Google Protocol Buffers
import grpc # Импорт библиотеки для работы с gRPC
import order_management_pb2 # Импорт сгенерированных файлов protobuf
import order_management_pb2_grpc
import time # Импорт библиотеки для работы со временем

# Определение основной функции run, которая запускает клиент
def run():
    channel = grpc.insecure_channel('localhost:50051') # Установка соединения с gRPC сервером на localhost на порту 50051
    stub = order_management_pb2_grpc.OrderManagementStub(channel) # Создание stub (клиентского прокси) для сервиса управления заказами

    # Создание заказа
    order1 = order_management_pb2.Order(items=['Item - A', 'Item - B', 'Item - C'],price=2450.50,description='This is a Sample order - 1 : description.',destination='San Jose, CA')


    order = stub.getOrder(order_management_pb2.Order(id='101')) # Вызов метода getOrder для получения заказа с id '101'
    print("Order service response", order) # Вывод полученного заказа


    response = stub.addOrder(order1) # Добавление заказа через вызов метода addOrder
    print('Add order response :', response) # Вывод ответа сервера после добавления заказа

    for order_search_result in stub.searchOrders(wrappers_pb2.StringValue(value='Item - A')): # Серверный стриминг: поиск заказов, содержащих 'Item - A'
        print('Search Result : ', order_search_result) # Вывод каждого найденного результата

    upd_order_iterator = generate_orders_for_updates() # Клиентский стриминг: отправка обновлений заказов
    upd_status = stub.updateOrders(upd_order_iterator)
    print('Order update status : ', upd_status) # Вывод статуса обновления заказов

    proc_order_iterator = generate_orders_for_processing() # Двунаправленный стриминг: обработка заказов
    for shipment in stub.processOrders(proc_order_iterator):
        print(shipment) # Вывод информации о каждой отправке

def generate_orders_for_updates(): # Функция для генерации обновлённых заказов для отправки на сервер
    # Создание нескольких заказов
    ord1 = order_management_pb2.Order(id='101', price=1000, items=['Item - A', 'Item - B', 'Item - C', 'Item - D'], description='Sample order description.', destination='Mountain View, CA')
    ord2 = order_management_pb2.Order(id='102', price=1000, items=['Item - E', 'Item - Q', 'Item - R', 'Item - D'], description='Sample order description.', destination='San Jose, CA')
    ord3 = order_management_pb2.Order(id='103', price=1000, items=['Item - A', 'Item - K'], description='Sample order description.', destination='San Francisco, CA')
    list = [] # Список для хранения заказов
    # Добавление заказов в список
    list.append(ord1)
    list.append(ord2)
    list.append(ord3)

    for updated_orders in list: # Итератор для отправки обновлённых заказов
        yield updated_orders

def generate_orders_for_processing(): # Функция для генерации заказов для обработки и отправки на сервер
    # Создание заказов
    ord1 = order_management_pb2.Order(id='104', price=2332, items=['Item - A', 'Item - B'], description='Updated desc', destination='San Jose, CA')
    ord2 = order_management_pb2.Order(id='105', price=3000, description='Updated desc', destination='San Francisco, CA')
    ord3 = order_management_pb2.Order(id='106', price=2560, description='Updated desc', destination='San Francisco, CA')
    ord4 = order_management_pb2.Order(id='107', price=2560, description='Updated desc', destination='Mountain View, CA')

    list = [] # Список для хранения заказов
    list.append(ord1)  #Добавление заказов в список
    list.append(ord2)
    list.append(ord3)
    list.append(ord4)

    for processing_orders in list: # Итератор для отправки заказов на обработку
        yield processing_orders

run() #Запуск программы