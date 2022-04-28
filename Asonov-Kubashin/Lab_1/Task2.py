def boolean(array):
    length = len(array)
    # цикл по маскам
    for n in range(1, 2**length):
        b = ""
        # перевод маски в двоичную сс
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        while len(b) < length:
            b = '0'+b
        j = 0
        temp = {}
        temp = set(temp)
        for i in array:
            if b[j] == "1":
                temp.add(i)
            j += 1
        print(*temp)