# Wezel drzewa
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # czestotliwosc
        self.symbol = symbol  # nazwa
        self.left = left  # lewy wezel
        self.right = right  # prawy wezel
        self.huff = ''  # kierunek (1/0)


def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

    # if node is edge node then
    # display its huffman code
    if (not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")


