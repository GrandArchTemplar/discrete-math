def reflexivity(l: [[]], m: int) -> bool:
    t = 0
    for i in range(len(l)):
        if l[i][0] == l[i][1]:
            t = t + 1
    if t == m:
        return True
    else:
        return False


def symmetry(l: [[]]) -> bool:
    for i in range(len(l)):
        t = 0
        for j in range(len(l)):
            if l[i][0] == l[j][1] and l[i][1] == l[j][0]:
                t = t + 1
        if t == 0:
            return False
    return True


def transitivity(l: [[]]):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][1] == l[j][0]:
                t = 0
                for k in range(len(l)):
                    if l[i][0] == l[k][0] and l[j][1] == l[k][1]:
                        t = t + 1
                if t == 0:
                    return False
    return True


print('Input:')
inp1 = str(input())
inp1 = inp1.split(' ')
m = int(inp1[0])
n = int(inp1[1])

inp2 = []
for i in range(n):
    inp2.append(str(input()))

inp2_sol = []
for i in range(n):
    inp2_sol.append(inp2[i].split(' '))

if symmetry(inp2_sol):
    print('симметричности')
else:
    print('антисимметричности')

if transitivity(inp2_sol):
    print('транзитивности')
else:
    print('антитранзитивности')

if reflexivity(inp2_sol, m):
    print('рефлексивности')
else:
    print('антирефлексивности')
