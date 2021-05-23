# Czesc kodu na podstawie https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/.

# Wezel drzewa
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # czestotliwosc
        self.symbol = symbol  # nazwa
        self.left = left  # lewy wezel
        self.right = right  # prawy wezel
        self.huff = ''  # kierunek (1/0)


# metoda do wypisywania wezlow
def printNodes(node, val=''):
    newVal = val + str(node.huff)

    # Jesli wezel nie jest lisciem, wejdź glebiej
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    # Jesli wezel jest lisciem, wyswietl jego kod
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")


# funkcja zwraca wartosci bitowe dla konkretnego znaku
def getValue(node, sign, val=''):
    newVal = val + str(node.huff)
    val = None
    # Jesli wezel nie jest lisciem, wejdź glebiej
    if node.left:
        temp1 = getValue(node.left, sign, newVal)
        if temp1 is not None:
            val = temp1
    if node.right:
        temp2 = getValue(node.right, sign, newVal)
        if temp2 is not None:
            val = temp2
    # Jesli wezel jest lisciem, wyswietl jego kod
    if not node.left and not node.right:
        if node.symbol == sign:
            return newVal
    else:
        return val


# funkcja dekoduje wiadomosc na stringa
def decode(node, bits):
    root = node  # zapamietaj korzen
    message = ''  # miejsce na wiadomosc
    for i in range(len(bits)):
        bit = bits[i]  # bit wiadomosci
        if bit == '0':  # jezeli 0 to wez wezel z lewej strony
            node = node.left
        else:  # jezeli 1 to wez wezel z prawej strony
            node = node.right
        # jezeli wezel nie ma dzieci to dopisz symbol do wiadomosci
        if not node.left and not node.right:
            message += node.symbol
            node = root  # ustaw korzen jako wezel
    return message
