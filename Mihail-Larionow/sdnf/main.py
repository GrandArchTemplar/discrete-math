if __name__ == '__main__':
    s = ""
    sym = ["a", "b", "c", "d", "e"]
    k = int(input())
    for i in range(2 ** k):
        l = list(map(int, input().split()))
        if l[-1]:
            if s != "": s += "+"
            for j in range(len(l) - 1):
                if j != 0: s += "^"
                if l[j]:
                    s += sym[j]
                else:
                    s = s + "(-" + sym[j] + ")"
    print(s)