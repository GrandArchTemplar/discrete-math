import sys


def dfs(u, destination, visited, graph):
    if (u == destination):
        return 0
    visited[u] = 1
    ans = INF
    for i in range(V):
        if (graph[u][i] != INF and not visited[i]):
            curr = dfs(i, destination, visited, graph)

            if (curr < INF):
                ans = min(ans, graph[u][i] + curr)

    visited[u] = 0
    return ans


if __name__ == "__main__":

    INF = sys.maxsize
    n, m, k = map(int, input().split(' '))
    V = m + 1
    graph = [[INF for j in range(V)] for i in range(V)]
    visited = [0 for i in range(V)]
    source = k
    visited[source] = 1

    for i in range(m):
        a, b, c = map(int, input().split(' '))
        graph[a][b] = c

    for dest in range(1, n + 1):
        print(dfs(source, dest, visited, graph), end=' ')