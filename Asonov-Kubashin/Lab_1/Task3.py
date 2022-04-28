"""
Gроверятор по данному графу его симметричности, транзитивности,
рефлексивности, антитранзитивности, антирефлексивности, антисимметричности
"""

def Graph():
    array_A = list(map(int, input("Введите через пробел число вершин графа и число его рёбер: ").split(" ")))

    links = [[False for i in range(array_A[1])] for i in range(array_A[1])]
    for i in range(array_A[1]):
        array = input().split(" ")
        links[int(array[0])][int(array[1])] = True
    IsTransitive(links)
    IsReflexive(links)
    IsSymmetric(links)
    pass


def IsReflexive(links: list):
    count = 0
    for i in range(len(links)):
        if links[i][i]:
            count += 1
    if count == len(links):
        print("Рефлексивный - абсолютно для всех элементов")
    elif count > 0:
        print("Нерефлексивный - не для всех элементов")
    else:
        print("Антирефлексивный - вообще ни для каких элементов")
    pass


def IsTransitive(links):
    l = len(links)
    true = 0
    false = 0
    for i in range(l):
        for j in range(l):
            if links[i][j] and i != j:
                for k in range(l):
                    if k != i and links[i][k] and links[j][k]:
                        true += 1
                    else:
                        false += 1
    if false == l:
        print("Антитранзитивный - вообще ни для каких элементов")
        return 0
    elif true == l:
        print("Транзитивный - абсолютно для всех элементов")
    else:
        print("Нетранзитивный - не для всех элементов")


def IsSymmetric(links):
    l = len(links)
    count = 0
    for i in range(l):
        for j in range(l):
            if i != j and links[i][j] and links[j][i]:
                count += 1
    if count == l:
        print("Симметричный - абсолютно для всех элементов")
    elif count == 0:
        print("Антисимметричный - вообще ни для каких элементов")
    else:
        print("Несимметричный - не для всех элементов")
