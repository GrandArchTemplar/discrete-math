if __name__ == '__main__':
    graph = {}
    weights = []

    n, m, k = map(int, input().split(' '))
    for i in range(n):
        graph[i + 1] = []
        weights.append([])
        for j in range(n):
            weights[i].append(0)
    for i in range(m):
        f, t, w = map(int, input().split(' '))
        graph[f].append(t)
        weights[f - 1][t - 1] = w


    def dfs(graph, from_v, to_v):
        path = 0
        stack = [(from_v, path)]
        while stack:
            (vertex, path) = stack.pop()
            if vertex == to_v:
                yield path
            if path <= n * 2:
                for next in graph[vertex]:
                    if next == to_v:
                        yield path + weights[vertex - 1][next - 1]
                    else:
                        stack.append((next, path + weights[vertex - 1][next - 1]))


    for i in range(len(graph)):
        paths = list(dfs(graph, k, i + 1))
        if paths == []:
            print("-", end=' ')
        else:
            print(min(paths), end=' ')