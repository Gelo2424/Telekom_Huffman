import socket

socketObject = socket.socket()

# Polacz sie z serwerem
socketObject.connect(("localhost", 35491))
print("Lacznie z localhostem")

# Send a message to the web server to supply a page as given by Host param of GET request
HTTPMessage = "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"
bytes = str.encode(HTTPMessage)
socketObject.sendall(bytes)

# Odbierz dane
while (True):
    data = socketObject.recv(1024)
    print(data)
    if (data == b''):
        print("Connection closed")
        break

socketObject.close()