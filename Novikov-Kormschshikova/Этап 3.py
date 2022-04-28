graph_sets = list(map(int, input().split()))
graphs = []
for i in range(graph_sets[1]):
    graphs.append(list(map(int, input().split())))

reflexive_count = 0
for graph in graphs:
    if graph[0] == graph[1]:
        reflexive_count += 1
if reflexive_count == graph_sets[0]:
    print("рефлексивно")
elif reflexive_count == 0:
    print("антирефлексивно")

symmetric_count = 0
for i in range(len(graphs)):
    for j in range(len(graphs)):
        if (graphs[i][0] == graphs[j][1]) and (graphs[i][1] == graphs[j][0]):
            symmetric_count += 1
if symmetric_count == len(graphs):
    print("симметрично")
elif symmetric_count == 0:
    print("антисимметрично")

transitive_count = 0
for i in range(len(graphs)):
    for j in range(len(graphs)):
        for k in range(len(graphs)):
            if (graphs[i][1] == graphs[j][0]) and ([graphs[i][0], graphs[j][1]] == graphs[k]):
                transitive_count += 1
if transitive_count == len(graphs):
    print("транзитивно")
elif transitive_count == 0:
    print("антитранзитивно")