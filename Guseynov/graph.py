def simm(ex_top, ex_edge):
    sim_edge = []
    for i in ex_edge:
        sim_edge.append([i[1], i[0]])

    if sorted(ex_edge) == sorted(sim_edge):
        return "Симметрично"
    else:
        c_s = 0
        c_a = 0
        for i in sim_edge:
            if i in ex_edge:
                if i[0] == i[1]:
                    c_s += 1
                else:
                    c_a += 1

        if c_a != 0:
            return "Несимметрично"
        return "Антисимметрично"

def trans(ex_edge):
  second_el = []
  for (a, b) in ex_edge:
    second_el.append(b)
    for (a, b) in ex_edge:
        for c in second_el:
            if (b, c) in ex_edge and (a, c) not in ex_edge:
                return "Нетранзитивно"
    return "Транзитивно"

def reflex(ex_top, ex_edge):
    ref_top = []
    c = 0
    for i in ex_top:
        ref_top.append([i, i])
    for i in ref_top:
        if i in ex_edge:
            c += 1

    if c == len(ex_top):
        return "Рефлексивно"
    elif c == 0:
        return "Антирефлексивно"
    return "Нерефлексивно"



if __name__=='__main__':
    top, edges = map(int, input().split())
    existing_top = []
    for i in range(top):
        existing_top.append(i)
    existing_edge = []
    for i in range(edges):
        existing_edge.append(list(map(int, input().split())))
    print(simm(existing_top, existing_edge))
    print(trans(existing_edge))
    print(reflex(existing_top, existing_edge))