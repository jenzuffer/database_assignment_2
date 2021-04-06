from huffmantree import Huffmantree

bits_size = 0

def run_example1():
    chars = ['a', 'b', 'c', 'd', 'e', 'f']

    # frequency of charecters
    freq = [ 5, 9, 12, 13, 16, 45]

    # list containing unused nodes
    nodes = []
    for x in range(len(chars)):
        nodes.append(Huffmantree(freq[x], chars[x]))
    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newnode = Huffmantree(left.freq + right.freq, left.symbol + right.symbol, left, right)
        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newnode)
    printNodes(nodes[0])
    global bits_size
    bits_size = 0

def run_example3():
    global bits_size
    bits_size = 0
    str1 = "pete is here"
    freq = [1, 4, 1, 1, 1, 1]
    nodes = []
    for chars in str1:
        for x in range(len(chars)):
            nodes.append(Huffmantree(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newnode = Huffmantree(left.freq + right.freq, left.symbol + right.symbol, left, right)
        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newnode)
    printNodes(nodes[0])

def run_example4():
    str1 = "this is a longer str sentence after all"
    freq = [4, 1, 2, 4, 3, 3, 1, 3, 1, 4, 3]
    nodes = []
    for chars in str1:
        for x in range(len(chars)):
            nodes.append(Huffmantree(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newnode = Huffmantree(left.freq + right.freq, left.symbol + right.symbol, left, right)
        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newnode)
    printNodes(nodes[0])

def run_example2():
    str1 = "beebs beepps!!!!!  their eerie ears hear pears"
    #figure out frequency
    freq = [3, 10, 4, 3, 5, 1, 2, 5, 2]

    nodes = []
    for chars in str1:
        for x in range(len(chars)):
            nodes.append(Huffmantree(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newnode = Huffmantree(left.freq + right.freq, left.symbol + right.symbol, left, right)
        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newnode)
    printNodes(nodes[0])
    global bits_size
    print("compressed total size?")
    print(bits_size)
    print("raw ascii bit")
    print(utf8len(str1))
    

def utf8len(s):
    return len(s.encode('utf-8'))

def main():
    run_example1()
    print("\n\n")
    run_example2()
    print("\n\n")
    run_example3()
    print("\n\n")
    run_example4()

def printNodes(node, val=''):
    global bits_size
    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)

        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
        bits_size += utf8len(node.symbol)

if __name__ == "__main__":
    main()
