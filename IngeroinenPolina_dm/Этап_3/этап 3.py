# Написать проверятор по данному графу его симметричности, транзитивности, рефлексивности,
# антитранзитивности, антирефлексивности, антисимметричности
# Формат ввода: два числа. Первое --- число вершин в графе.
# Второе --- число ребер. Далее идет список из ребер, каждое из которых соединяет пару чисел. Ребра нумеруются с 0.4

def symmetric(para_rib):
    pairs = []
    for i in para_rib:
        pairs.append([i[1], i[0]])
    if sorted(pairs) == sorted(para_rib):
        return "симметрично"
    else:
        return "антисимметрично"

def transitiv(para_rib):
    second_element = []
    for (a, b) in para_rib:
        second_element.append(b)
        for (a, b) in para_rib:
            for c in second_element:
                if (b, c) in para_rib and (a, c) in para_rib:
                    return "транзитивно"
                elif (a == b) and (b == c):
                    return "транзитивно"
                else:
                    return "антитранзитивно"

def reflex(para_rib):
    ref_ver = []
    S = 0
    for i in col_ver:
        ref_ver.append([i, i])
    for j in ref_ver:
        if j in para_rib:
            S += 1
    if S == len(col_ver):
        return "рефлексивно"
    else:
        return "антирефлексивно"

verhina, rib = map(int, input().split())
col_ver = []
for i in range(verhina):
  col_ver.append(i)
par_rib = []
for i in range(rib):
  par_rib.append(list(map(int, input().split())))

print(reflex(par_rib))
print(symmetric(par_rib))
print(transitiv(par_rib))