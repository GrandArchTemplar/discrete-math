def simm(ex_versh, ex_reb):
    sim_reb = []
    for i in ex_reb:
        sim_reb.append([i[1], i[0]])

    if sorted(ex_reb) == sorted(sim_reb):
        a = "Симметрично"
    else:
        k_sim_reb = 0
        k_nesim_reb = 0

        for i in sim_reb:
            if i in ex_reb:
                if i[0] == i[1]:
                    k_sim_reb += 1
                else:
                    k_nesim_reb += 1

        if k_nesim_reb != 0:
            a = "Несимметрично"
        else:
            a = "Антисимметрично"
    return a

def trans(ex_reb):
  second_el = []
  for (a, b) in ex_reb:
    second_el.append(b)
    for (a, b) in ex_reb:
        for c in second_el:
            if (b, c) in ex_reb and (a, c) not in ex_reb:
                return "Нетранзитивно"
    return "Транзитивно"

def reflex(ex_versh, ex_reb):
    ref_versh = []
    k = 0
    for i in ex_versh:
        ref_versh.append([i, i])
    for i in ref_versh:
        if i in ex_reb:
            k += 1

    if k == len(ex_versh):
        return "Рефлексивно"
    elif k == 0:
        return "Антирефлексивно"
    else:
        return "Нерефлексивно"



versh, edges = map(int, input().split())

existing_versh = []
for i in range(versh):
  existing_versh.append(i)

existing_reb = []
for i in range(edges):
  existing_reb.append(list(map(int, input().split())))

if __name__=='__main__':
    print(simm(existing_versh, existing_reb))
    print(trans(existing_reb))
    print(reflex(existing_versh, existing_reb))