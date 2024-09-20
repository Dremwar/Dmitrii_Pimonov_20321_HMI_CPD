#Импортируем библиотеки
from concurrent import futures #для асинхронного выполнения задач.
import time # Импорт библиотеки для работы со временем
from typing import OrderedDict
import uuid #Уникальные индефикаторы заказов
from google.protobuf import wrappers_pb2#Для работы с различными типами значений
import grpc #для создания gRPC-сервера
import order_management_pb2_grpc #сгенерированных gRPC файлы
import order_management_pb2

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer): #Класс наследует функциональность gRPC сервиса для работы с заказами

    def __init__(self):
        self.orderDict = {}
        # Создаём и добавляем примеры в выше созданный словарь
        self.orderDict['101'] = order_management_pb2.Order(id='101', price=1000,items=['Item - A', 'Item - B'], description='Sample order description.')
        self.orderDict['102'] = order_management_pb2.Order(id='102', price=1000,items=['Item - C'], description='Sample order description.')
        self.orderDict['103'] = order_management_pb2.Order(id='103', price=1000,items=['Item - A', 'Item - E'], description='Sample order description.')
        self.orderDict['104'] = order_management_pb2.Order(id='104', price=1000,items=['Item - F', 'Item - G'], description='Sample order description.')

    def getOrder(self, request, context): # Метод для обработки унарного RPC запроса на получение заказа по ID
        order = self.orderDict.get(request.value) # Поиск заказа по ID
        if order is not None:
            return order
        else:
            # Обработка ошибки, если заказ не найден.
            print('Order not found ' + request.value)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Order : ', request.value, ' Not Found.')
            return order_management_pb2.Order()

    # Метод для обработки унарного RPC запроса на добавление заказа
    def addOrder(self, request, context):
        id = uuid.uuid1() # Генерация уникального идентификатора для нового заказа
        request.id = str(id)
        self.orderDict[request.id] = request
        response = wrappers_pb2.StringValue(value=str(id)) # Формирование и возврат ответа с ID заказа
        print(self.orderDict)
        return response

    # Метод для обработки поиска заказов по ключевому слову
    def searchOrders(self, request, context):
        matching_orders = self.searchInventory(request.value) # Получение соответствующих заказов
        for order in matching_orders: # Возвращение каждого соответствующего заказа
            yield order

    # Метод для обработки обновления ID заказов поступающих со стороны клиента
    def updateOrders(self, request_iterator, context):
        response = 'Updated IDs :'
        for order in request_iterator: # Обновление каждого заказа в итераторе
            self.orderDict[order.id] = order
            response += ' ' + order.id
        return wrappers_pb2.StringValue(value=response) # Возврат строки с обновлёнными ID заказов

    # Метод для обработки двунаправленого мониторинга заказов
    def processOrders(self, request_iterator, context):
        print('Processing orders.. ')
        shipment_id = uuid.uuid1() # Генерация уникального ID для отправления
        shipments = [] # Инициализация списка отправлений

        shipment = order_management_pb2.CombinedShipment(id=str(shipment_id), status='PROCESSED', ) # Создание объекта отправления
        shipments.append(shipment)
        for order_id in request_iterator: # Возвращение информации об отправлении для каждого заказа в итераторе
            for order in shipments:
                yield order

    # Функция для поиска заказов по элементу
    def searchInventory(self, query):
        matchingOrders = [] # Инициализация списка соответствующих заказов
        for order_id, order in self.orderDict.items(): # Перебор всех заказов и поиск соответствий
            for itm in order.items:
                if query in itm:
                    matchingOrders.append(order)
                    break
        return matchingOrders # Возврат списка соответствующих заказов


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server) # Добавление сервиса управления заказами на сервер
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051') # Назначение порта для прослушивания сервером
server.start()
server.wait_for_termination()