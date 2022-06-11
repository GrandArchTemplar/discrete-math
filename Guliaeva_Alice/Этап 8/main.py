from queue import deque
if __name__ == '__main__':
    graph = {}
    paths = []

    n, m, k = map(int, input().split(' '))
    for i in range(n):
        graph[i + 1] = []
        paths.append([])
        for j in range(n):
            paths[i].append(0)
    for i in range(m):
        a, b, c = map(int, input().split(' '))
        graph[a].append(b)
        paths[a - 1][b - 1] = c

    def bfs(graph, from_v, to_v):
        path = 0
        queue = deque([(from_v, path)])
        while queue:
            (ver, path) = queue.pop()
            if ver == to_v:
                yield path
            if path <= n * 2:
                for next in graph[ver]:
                    if next == to_v:
                        yield path + paths[ver - 1][next - 1]
                    else:
                        queue.appendleft((next, path + paths[ver - 1][next - 1]))

    for i in range(len(graph)):
        path_2 = list(bfs(graph, k, i + 1))
        if path_2 == []:
            print(" ", end=' ')
        else:
            print(min(path_2), end=' ')
