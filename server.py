import socket


def openServerSocket():
    serverSocket = socket.socket()
    print("Gniazdo serwera utworzone")

    # Powiazanie serwera z adresm ip i portem
    ip = "127.0.0.1"
    port = 35491
    serverSocket.bind((ip, port))
    print("Gniazdo serwera - ip {} port {}".format(ip, port))

    # Nasluchuj
    serverSocket.listen()

    # Przychodzace polaczenia (jedno za drugim)
    count = 0
    while True:
        (clientConnection, clientAddress) = serverSocket.accept()
        count = count + 1
        print("Zaakceptowano {} poleczen".format(count))
        # Czytaj od klienta
        while True:
            data = clientConnection.recv(1024)
            print("Otrzymany pakiet: ")
            print(data)
            if data != b'':
                print("Connection closed")
                return data
