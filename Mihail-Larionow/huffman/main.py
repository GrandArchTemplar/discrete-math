import heapq
from collections import Counter, namedtuple


class Tree(namedtuple("Tree", ["left","right"])):
    def walk(self, huffman_code, acc):
        self.left.walk(huffman_code, acc + "0")
        self.right.walk(huffman_code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, huffman_code, acc):
        huffman_code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    h_count = len(h)
    while len(h) > 1:
        freqleft, countleft, left = heapq.heappop(h)
        freqright, countright, right = heapq.heappop(h)
        heapq.heappush(h, (freqleft+freqright, h_count, Tree(left, right)))
        h_count += 1
    huffman_code = {}
    if h:
        [(h_freq, h_count, root)] = h
        root.walk(huffman_code, "")
    return huffman_code


if __name__ == '__main__':
    s = input()
    h_code = huffman_encode(s)
    encoded = "".join(h_code[ch] for ch in s)
    for ch in sorted(h_code):
        print("{}: {}".format(ch, h_code[ch]))