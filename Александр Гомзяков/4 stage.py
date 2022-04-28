

import heapq
from collections import Counter, namedtuple

class Tree(namedtuple("Node", ["left", "right"])):
    def walk(self, enter, acc):
        self.left.walk(enter, acc + "0")
        self.right.walk(enter, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, enter, acc):
        enter[self.char] = acc or "0"

def huffman_encode(s):
    h = []
    for sim, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(sim)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Tree(left, right)))
        count += 1
    enter = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(enter, "")
    return enter

def main():
    s = input()
    enter = huffman_encode(s)
    for sim in sorted(enter):
        print("{}: {}".format(sim, enter[sim]))

if __name__ == "__main__":
    main()