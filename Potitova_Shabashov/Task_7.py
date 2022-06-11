if __name__ == '__main__':
    rebro = []
    graph = {}

    n, m, k = map(int, input().split(' '))
    for i in range(n):
        rebro.append([])
        graph[i + 1] = []
        for j in range(n):
            rebro[i].append(0)
    for i in range(m):
        f, t, r = map(int, input().split(' '))
        rebro[f - 1][t - 1] = r
        graph[f].append(t)

    def dfs(graph, f_v, t_v):
        w = 0
        p = [(f_v, w)]
        while p:
            (versh, w) = p.pop()
            if versh == t_v:
                yield w
            if w <= n * 2:
                for sl in graph[versh]:
                    if sl != t_v:
                        p.append((sl, w + rebro[versh - 1][sl - 1]))
                    else:
                        yield w + rebro[versh - 1][sl - 1]


    print()
    for i in range(len(graph)):
        w = list(dfs(graph, k, i + 1))
        if w != []:
            print(min(w), end=' ')
        else:
            print("-", end=' ')