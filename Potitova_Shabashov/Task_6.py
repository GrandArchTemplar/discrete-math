s = ''
f = False
k = int(input())
for i in range(0, 2**k):
    a = input().split()
    if a[k] == '0':
        if f:
            s += ') and '
        f = True
        if a[0] == '0':
            s += '(' + chr(65)
        else:
            s += '(not ' + chr(65)
        for j in range(1, k):
            if a[j] == '0':
                s += ' or ' + chr(65+j)
            else:
                s += ' or not ' + chr(65+j)
if f:
    s += ')'
print(s)