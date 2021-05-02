from huffman import *

signs = []
freq = []

with open("send") as file:
    for line in file:
        for sign in line:
            if sign not in signs:
                signs.append(sign)
                freq.append(0)
                freq[signs.index(sign)] += 1
            else:
                freq[signs.index(sign)] += 1

print(signs)
print(freq)

# list containing unused nodes
nodes = []

# converting ccharecters and frequencies
# into huffman tree nodes
for x in range(len(signs)):
    nodes.append(node(freq[x], signs[x]))

while len(nodes) > 1:
    # sort all the nodes in ascending order
    # based on theri frequency
    nodes = sorted(nodes, key=lambda x: x.freq)

    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]

    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1

    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    # remove the 2 nodes and add their
    # parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

# Huffman Tree is ready!
printNodes(nodes[0])

