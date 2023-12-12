import socket
import pickle
import protolc_pb2
import time

tempev = protolc_pb2.TempEvent()
tempev.device_id = 1234
tempev.event_id = 4321
tempev.humidity = 2.6
tempev.temp_cel = 3.1415

a = tempev.SerializeToString()

sock = socket.socket()
SERVER_IP = 'localhost'
SERVER_PORT = 12345

sock.connect((SERVER_IP, SERVER_PORT))

while True:
    try:

        time.sleep(1)
        sock.send(a)
        

       # time.sleep(1)
        #sock.send(pickle.dumps(data_pick, pickle.HIGHEST_PROTOCOL))
    except KeyboardInterrupt:
        break

sock.close()