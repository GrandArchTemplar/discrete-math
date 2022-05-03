if __name__ == '__main__':
    s = ""
    sym = ["a", "b", "c", "d", "e"]
    k = int(input())
    for i in range(2 ** k):
        l = list(map(int, input().split()))
        if not(l[-1]):
            s += "("
            for j in range(len(l) - 1):
                if j != 0: s += " + "
                if not(l[j]):
                    s += sym[j]
                else:
                    s = s + "-" + sym[j]
            s += ")"
    print(s)