print("Input:")
Ip1 = int(input())
symb_main = 'a b c d e'
symb_main = symb_main.split(' ')
symb = []
for i in range(Ip1):
    symb.append(symb_main[i])

Ip2 = []
for i in range(2**Ip1):
    Ip2.append(str(input()).split(' '))

Out = ''
for i in range(2**Ip1):
    if Ip2[i][Ip1] == '0':
        Out = Out + '('
        for j in range(Ip1):
            if Ip2[i][j] == '0':
                Out = Out + '-'
            Out = Out + symb[j] + ' + '
        Out = Out[:(len(Out) - 3)] + ')'

print('Output:')
print(Out)
