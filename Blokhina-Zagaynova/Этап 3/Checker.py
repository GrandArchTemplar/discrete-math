def reflexivity(pts, edgs):
    count = 0
    rflx_edges = [[i, i] for i in range(len(pts))]
    for i in rflx_edges:
        if i in edgs:
            count += 1

    if count == len(pts):
        return "рефлексивно"
    elif count == 0:
        return "антирефлексивно"
    else:
        return "нерефлексивно"

def symmetry(edgs):
    count = 0
    invrt_edges = [[i[1], i[0]] for i in edgs]
    for i in invrt_edges:
        if i in edgs:
            count += 1

    if count == len(edgs):
        return "симметрично"
    elif count == 0:
        return "антисимметрично"
    else:
        return "несимметрично"

def transitivity(edgs):
    trns, anti_trns = True, True
    c_arr = [j for (i, j) in edgs]
    for (a, b) in edgs:
        for c in c_arr:
            if (b, c) in edgs and (a, c) in edgs:
                anti_trns = False
        for c in c_arr:
            if (b, c) in edgs and (a, c) not in edgs:
                trns = False

    if not anti_trns:
        if trns:
            return "транзитивно"
        else:
            return "нетранзитивно"
    else:
        return "антитранзитивно"


n, m = map(int, input().split())
points, edges = [], []
for i in range(n):
    points.append(i)
for j in range(m):
    edges.append(list(map(int, input().split())))

print(symmetry(edges))
print(transitivity(edges))
print(reflexivity(points, edges))

