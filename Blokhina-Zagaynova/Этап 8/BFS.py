from collections import deque


class Graph:

    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(2 * n)]

        for (v, u, weight) in edges:

            if weight == 2:
                self.adjList[v].append(v + n)
                self.adjList[v + n].append(u)

            else:
                self.adjList[v].append(u)


def path(predecessor, v, cost, n):
    if v >= 0:
        cost = path(predecessor, predecessor[v], cost, n)
        cost = cost + 1

    return cost


def bfs(graph, source, dest, n):
    discovered = [False] * 2 * n
    discovered[source] = True
    predecessor = [-1] * 2 * n
    q = deque()
    q.append(source)

    while q:

        curr = q.popleft()

        if curr == dest:
            print(path(predecessor, dest, -1, n), end=' ')

        for v in graph.adjList[curr]:
            if not discovered[v]:
                discovered[v] = True
                q.append(v)
                predecessor[v] = curr


if __name__ == '__main__':

    n, m, k = map(int, input().split(' '))
    edges = []
    source = k

    for i in range(m):
        a, b, c = map(int, input().split(' '))
        edges.append([a, b, c])

    graph = Graph(edges, n)
    for dest in range(1, n + 1):
        bfs(graph, source, dest, n)