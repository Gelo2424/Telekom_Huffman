import socket

serverSocket = socket.socket()
print("Server socket created")

# Powiazanie serwera z adresm ip i portem
ip = "127.0.0.1"
port = 35491
serverSocket.bind((ip, port))
print("Gniazdo serwera - ip {} port {}".format(ip, port))

# Nasluchuj
serverSocket.listen()

# Przychodzace polaczenia (jedno za drugim)
count = 0
while (True):
    (clientConnection, clientAddress) = serverSocket.accept()
    count = count + 1
    print("Zaakceptowania {} poleczen".format(count))
    # Czytaj od klienta
    while (True):
        data = clientConnection.recv(1024)
        print(data)
        if (data != b''):
            msg1 = "Hi Client! Read everything you sent"
            msg1Bytes = str.encode(msg1)
            msg2 = "Now I will close your connection"
            msg2Bytes = str.encode(msg2)
            clientConnection.send(msg1Bytes)
            clientConnection.send(msg2Bytes)
            print("Connection closed")
            break