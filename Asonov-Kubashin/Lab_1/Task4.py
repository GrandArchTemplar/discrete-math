import heapq
from collections import Counter, namedtuple


class Tree(namedtuple("Tree", ["left","right"])):
    def walk(self, huffman_code, acc):
        self.left.walk(huffman_code, acc + "0")
        self.right.walk(huffman_code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, huffman_code, acc):
        huffman_code[self.char] = acc or "0"


def encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    h_count = len(h)
    while len(h) > 1:
        freq_left, count_left, left = heapq.heappop(h)
        freq_right, count_right, right = heapq.heappop(h)
        heapq.heappush(h, (freq_left + freq_right, h_count, Tree(left, right)))
        h_count += 1
    huffman_code = {}
    if h:
        [(h_freq, h_count, root)] = h
        root.walk(huffman_code, "")
    return huffman_code


def encode_string():
    s = input("Введите строку: ")
    h_code = encode(s)
    encoded = "".join(h_code[ch] for ch in s)
    for ch in sorted(h_code):
        print("{}: {}".format(ch, h_code[ch]))
