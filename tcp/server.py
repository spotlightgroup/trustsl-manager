from sockets.python3.server import Server
import json
from api.models import Transaction, ARQC, Merchant, Terminal, Card


class MyServer(Server):
    def act_on(self, data, addr):
        dec_data = data.decode()
        data_dic = json.loads(dec_data)
        insert_to_db(data_dic)
        return 'done'


def insert_to_db(data):
    card = Card.objects.get(no=data['card'])
    terminal = Terminal.objects.get(id=data['terminal'])
    arqc = ARQC.objects.get(id=data['arqc'])
    merchant = Merchant.objects.get(id=data['merchant'])

    transaction = Transaction(
        type=data['type'],
        date=data['date'],
        batch_no=data['batch_no'],
        ref_no=data['ref_no'],
        base=data['base'],
        tips=data['tips'],
        arqc=arqc,
        card=card,
        terminal=terminal,
        merchant=merchant,
        trace_no=data['trace_no'],
        app_code=data['app_code']
    )

    transaction.save()
    print(type(transaction.type))


def listen():
    port = int(input('choose port\nport:  '))
    server = MyServer(listening_address=('127.0.0.1', port))
    server.listen()
