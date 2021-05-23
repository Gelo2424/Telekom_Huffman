import socket


def openClientSocket(message):
    socketObject = socket.socket()
    # Polacz sie z serwerem
    socketObject.connect(("localhost", 35491))
    print("Polaczono z localhost")
    # Wyslij wiadomosc
    bytes = str.encode(message)
    socketObject.sendall(bytes)
    # Odbierz dane
    while True:
        data = socketObject.recv(1024)
        if data == b'':
            print("Connection closed")
            break
    socketObject.close()
