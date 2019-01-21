from sockets.python3.client import Client
import os.path
from req import REQUEST_JSON

DIR = os.path.abspath(os.path.join(os.pardir, 'tcpServer'))


client = Client()
response, addr = client.poll_server(REQUEST_JSON, server=('127.0.0.1', 4500))
print(response, addr)
