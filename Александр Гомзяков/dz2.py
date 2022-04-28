def symmetric(para_edge):    #функция проверки на симметричность
    pairs = []
    for i in para_edge:
        pairs.append([i[1], i[0]])
    if sorted(pairs) == sorted(para_edge):
        return "симметрично"
    else:
        return "антисимметрично"

def transitiv(para_edge):     #функция проверки на транзитивность
    g = []
    for (a, b) in para_edge:
        g.append(b)
        for (a, b) in para_edge:
            for c in g:
                if (b, c) in para_edge and (a, c) not in para_edge:
                    return "антитранзитивно"
        return "транзитивно"

def reflex(para_edge):      #функция проверки на рефлексивность
    ref_top = []
    S = 0
    for i in col_top:
        ref_top.append([i, i])
    for j in ref_top:
        if j in para_edge:
            S += 1
    if S == len(col_top):
        return "рефлексивно"
    else:
        return "антирефлексивно"

top, edge = map(int, input().split())  #top-вершина edge-ребро
col_top = []
for i in range(top):
  col_top.append(i)
par_edge = []
for i in range(edge):
  par_edge.append(list(map(int, input().split())))

print(symmetric(par_edge))
print(transitiv(par_edge))
print(reflex(par_edge))

