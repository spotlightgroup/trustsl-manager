from sockets.python3.server import Server
import json


class MyServer(Server):
    def act_on(self, data, addr):
        dec_data = data.decode()
        data_dic = json.loads(dec_data)
        insert_to_db(data_dic)
        return 'done'


def insert_to_db(data):
    print(data)


def listen():
    port = int(input('choose port\nport:  '))
    server = MyServer(listening_address=('127.0.0.1', port))
    server.listen()
