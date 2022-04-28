print('Input:')
input1 = str(input())
input1 = input1.split(' ')
m = int(input1[0])
n = int(input1[1])

input2 = str(input())
input2 = input2.split(' ')
a = []
for i in range(m):
    a.append(int(input2[i]))

input3 = str(input())
input3 = input3.split(' ')
b = []
for i in range(n):
    b.append(int(input3[i]))


def union(a: list, b: list) -> list:
    a1 = a
    for i in range(len(b)):
        t = 0
        for j in range(len(a)):
            if a[j] == b[i]:
                t = t + 1
        if t == 0:
            a1.append(b[i])
    return a1


def intersection(a: list, b: list) -> list:
    a1 = []
    for i in range(len(b)):
        t = 0
        for j in range(len(a)):
            if a[j] == b[i]:
                t = t + 1
        if t != 0:
            a1.append(b[i])
    return a1


def complement(b: list, a: list) -> list:
    a1 = []
    for i in range(len(b)):
        t = 0
        for j in range(len(a)):
            if a[j] == b[i]:
                t = t + 1
        if t == 0:
            a1.append(b[i])
    return a1


def symmetric_difference(a: list, b: list)  -> list:
    a1 = []
    a2 = intersection(a, b)
    a3 = union(a, b)
    for i in range(len(a3)):
        t = 0
        for j in range(len(a2)):
            if a3[i] == a2[j]:
                t = t + 1
        if t == 0:
            a1.append(a3[i])
    return a1


def list_style(a: list):
    a1 = []
    for i in range(len(a)):
        a1.append(str(a[i]))
    return a1


sign = str(input())
print('Output:')
if sign == 'u':
    print(' '.join(list_style(union(a, b))))
elif sign == 'p':
    print(' '.join(list_style(intersection(a, b))))
elif sign == '-':
    print(' '.join(list_style(complement(a, b))))
elif sign == 'a':
    print(' '.join(list_style(symmetric_difference(a, b))))
