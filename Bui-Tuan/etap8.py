from queue import Queue

class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Directed or Undirected
        self.m_directed = directed

        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}


    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))
    # Print the graph representation
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])


    def bfs(self, start_node, target_node):
        # Set of visited nodes to prevent loops
        visited = set()
        queue = Queue()

        # Add the start_node to the queue and visited list
        queue.put(start_node)
        visited.add(start_node)

        # start_node has not parents
        parent = dict()
        parent[start_node] = None

        # Perform step 3
        path_found = False
        while not queue.empty():
            current_node = queue.get()
            if current_node == target_node:
                path_found = True
                break
            for (next_node, weight) in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)

        # Path reconstruction
        path = []
        if path_found:
            path.append(target_node)
            while parent[target_node] is not None:
                path.append(parent[target_node])
                target_node = parent[target_node]
            path.reverse()
        return path


print('Input:')
input1 = str(input())
input1 = input1.split(' ')
for i in range(len(input1)):
    input1[i] = int(input1[i])
input2 = []
for i in range(input1[0]):
    input2.append(str(input()).split(' '))
for i in range(len(input2)):
    for j in range(len(input2[i])):
        input2[i][j] = int(input2[i][j])


t = int(input1[0]) + 1
in_gr = []
for i in range(len(input2)):
    if input2[i][2] == 1:
        in_gr.append([input2[i][0], input2[i][1]])
    if input2[i][2] == 2:
        in_gr.append([input2[i][0], t])
        in_gr.append([t, input2[i][1]])
        t = t + 1

graph = Graph(t-1, directed=True)
for i in range(len(in_gr)):
    graph.add_edge(int(in_gr[i][0]) - 1, int(in_gr[i][1]) - 1)

traversal_path = []
out = []
op = []
for i in range(input1[0]):
    traversal_path = graph.bfs(input1[2] -1, i)
    out.append([])
    for j in range(len(traversal_path)):
        out[i].append(traversal_path[j])

for i in range(len(out)):
    j = 0
    while j < len(out[i]):
        if out[i][len(out[i]) - j - 1] == input1[2] - 1:
            op.append(j)
            break
        j = j + 1
print('Output:')
print(op)
