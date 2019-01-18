import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4500
ip = '127.0.0.1'

if __name__ == "__main__":
    client.connect((ip, port))
    client.send('hello world'.encode())
    data = client.recv(1024)
