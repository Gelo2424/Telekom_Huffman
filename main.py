from huffman import *
from server import openServerSocket
from client import openClientSocket
import pickle

print("""
    # =================== #
    #  Grzegorz Kucharski #
    #       229932        #
    # =================== #
    """)

mode = None
correct = False
while correct is not True:
    print("""Wybierz tryb pracy programu:
    1 - klient
    2 - serwer""")
    try:
        # Wybieranie trybu pracy programu
        mode = int(input())
        if 0 < mode < 3:
            correct = True
        else:
            correct = False
    except ValueError:
        print("Bledny tryb")
        correct = False

if mode == 1:  # Jezeli wybrano tryb 1 - klient
    signs = []  # znaki
    freq = []   # czestotliwosc
    mess = []   # wiadomosc
    messBits = ''   # wiadomosc w bitach
    # fileName = str(input("Podaj nazwe pliku do wyslania: "))
    fileName = "send"   # tymczasowa nazwa pliku
    try:
        with open(fileName) as file:
            for line in file:   # czytaj linie
                for sign in line:   # czytaj znaki
                    if sign not in signs:   # jezeli nie ma znaku w signs to dopisz go i ustaw freq na 1
                        signs.append(sign)
                        freq.append(0)
                        mess.append(sign)
                        freq[signs.index(sign)] += 1
                    else:   # jezeli znak jest to dodaj +1 do freq
                        freq[signs.index(sign)] += 1
                        mess.append(sign)
    except IOError:
        print("Zla nazwa pliku")
        exit(1)

    # lista wezlow
    nodes = []
    # tworzenie nowych wezlow
    for x in range(len(signs)):
        nodes.append(node(freq[x], signs[x]))
    while len(nodes) > 1:
        # sortowanie rosnaco
        nodes = sorted(nodes, key=lambda x: x.freq)
        # 2 najmniejsze
        left = nodes[0]
        right = nodes[1]
        # 0 lub 1
        left.huff = 0
        right.huff = 1
        # laczenie dwoch najmniejszch wezlow by stworzyc nowy
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        # usun wezly, dodaj rodzica i jego dzieci
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    # Serializacja drzewa do pliku
    fileName = 'tree'
    file = open(fileName, 'wb')
    pickle.dump(nodes, file)
    file.close()

    # print(signs)
    # print(freq)
    # wyswietl drzewo
    printNodes(nodes[0])
    for i in range(len(mess)):
        messBits += getValue(nodes[0], mess[i])  # zamiana znakow na bity
    openClientSocket(messBits)  # funkcja do otwierania gniazda i wysylania wiadomosci

if mode == 2:  # jezeli wybrano tryb 2, czyli serwer
    data = openServerSocket().decode('ascii')  # odbierz wiadomosc z gniazda i zamien na stringa

    # wczytywanie drzewa z pliku
    fileName = 'tree'
    with open(fileName, 'rb') as file:
        nodes = pickle.load(file)
    file.close()

    message = decode(nodes[0], data)  # dekoduj odebrana wiadomosc i zapisz do pliku recive
    file = open("recive", "w")
    file.write(message)
    file.close()
