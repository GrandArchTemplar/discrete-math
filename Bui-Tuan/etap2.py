import itertools


def findsubsets(S, m):
    return list(itertools.combinations(S, m))


def list_style(a: list):
    a1 = []
    for i in range(len(a)):
        a1.append(str(a[i]))
    return a1


print('Input:')
n = int(input())
ip = str(input())
ip = ip.split(' ')
a = []
for i in range(n):
    a.append(int(ip[i]))

print('Output:')
b = []
for i in range(n):
    if i == 0:
        print('[]')
    else:
        b = list(findsubsets(a, i))
        for j in range(len(b)):
            print(' '.join(list_style(list(b[j]))))
print(' '.join(ip))
