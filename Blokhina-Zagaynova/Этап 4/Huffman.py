class Node(object):
    left = None
    right = None
    item = None
    weight = 0

    def __init__(self, symbol, weight, l=None, r=None):
        self.symbol = symbol
        self.weight = weight
        self.left = l
        self.right = r

    def __repr__(self):
        return '("%s", %s, %s, %s)' % (self.symbol, self.weight, self.left, self.right)


def sort_by_weight(node):
    return (node.weight * 1000000 + ord(node.symbol[0]))


class HuffmanEncoder:
    def __init__(self):
        self.symbols = {}
        self.codes = {}
        self.tree = []
        self.message = ""

    def frequency(self):
        self.symbols = {}
        for symbol in self.message:
            self.symbols[symbol] = self.symbols.get(symbol, 0) + 1

    def preorder_traverse(self, node, path=""):
        if node.left == None:
            self.codes[node.symbol] = path or "0"
        else:
            self.preorder_traverse(node.left, path + "0")
            self.preorder_traverse(node.right, path + "1")

    def encode(self, message):
        self.message = message
        self.frequency()
        self.tree = []

        for symbol in self.symbols.keys():
            self.tree.append((Node(symbol, self.symbols[symbol], None, None)))
        self.tree.sort(key=sort_by_weight)

        while len(self.tree) > 1:
            leftNode = self.tree.pop(0)
            rightNode = self.tree.pop(0)
            newNode = Node(leftNode.symbol + rightNode.symbol, leftNode.weight + rightNode.weight, leftNode, rightNode)
            self.tree.append(newNode)
            self.tree.sort(key=sort_by_weight)

        self.codes = {}
        self.preorder_traverse(self.tree[0])

        encodedMessage = ""
        for symbol in message:
            encodedMessage = encodedMessage + self.codes[symbol]

        return encodedMessage

    def Show(self):
        list = []
        for symbol in self.codes.keys():
            code = self.codes[symbol]
            list.append([len(code), symbol, code])
        list.sort()
        for code in list:
            print(code[1] + " " + code[2])


message = input()
encoder = HuffmanEncoder()
compressedMessage = encoder.encode(message)
encoder.Show()