#Алгоритм Хоффмана для строки

import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left_potom", "right_potom"])):
    def walk(self, clov, acc):
        self.left_potom.walk(clov, acc + "0")
        self.right_potom.walk(clov, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, clov, acc):
        clov[self.char] = acc or "0"

def huffman_encode(s):
    h = []
    for sim, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(sim)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left_potom = heapq.heappop(h)
        freq2, _count2, right_potom = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left_potom, right_potom)))
        count += 1
    clov = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(clov, "")
    return clov

def main():
    s = input()
    clov = huffman_encode(s)
    for sim in sorted(clov):
        print("{}: {}".format(sim, clov[sim]))

if __name__ == "__main__":
    main()
