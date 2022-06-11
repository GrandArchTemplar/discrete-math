graph = {}
weight_list = []
n, m, k = map(int, input().split(' '))

def dfs(graph, from_node, to_node):
    length = 0
    stack = [(from_node, length)]
    while stack:
        (node, length) = stack.pop()
        if node == to_node:
            yield length
        if length <= n * 2:
            for next in graph[node]:
                if next == to_node:
                    yield length + weight_list[node - 1][next - 1]
                else:
                    stack.append((next, length + weight_list[node - 1][next - 1]))

for i in range(n):
    graph[i + 1] = []
    weight_list.append([])
    for j in range(n):
        weight_list[i].append(0)

for i in range(m):
    frm, to, w = map(int, input().split(' '))
    graph[frm].append(to)
    weight_list[frm - 1][to - 1] = w

for i in range(len(graph)):
    lengths = list(dfs(graph, k, i + 1))
    if lengths == []:
        print("-", end=' ')
    else:
        print(min(lengths), end=' ')