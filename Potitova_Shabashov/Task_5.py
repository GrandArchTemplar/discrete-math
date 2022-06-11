s = ''
f = False
k = int(input())
for i in range(0, 2**k):
    a = input().split()
    if a[k] == '1':
        if f:
            s += ' or '
        f = True
        if a[0] == '1':
            s += chr(65)
        else:
            s += 'not ' + chr(65)
        for j in range(1, k):
            if a[j] == '1':
                s += ' and ' + chr(65+j)
            else:
                s += ' and not ' + chr(65+j)
print(s)