f = open('./inp.txt').read().split('\n')

caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lows = 'abcdefghijklmnopqrstuvwxyz'

graph = {}

for e in f:
    node1, node2 = e.split('-')
    if node1 in graph.keys():
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]

    if node2 in graph.keys():
        graph[node2].append(node1)
    else:
        graph[node2] = [node1]

visited = {k: False for k in graph.keys()}

paths = []


def traverse(graph, node, visited, path, s):
    global paths
    if not visited[node]:
        s += 1
        path.append(node)
        capsOrNot = [True if c in caps else False for c in node]
        if not all(capsOrNot):
            visited[node] = True
        if node == 'end':
            paths.append(path)
        else:
            neighbours = graph[node]
            for neighbour in neighbours:
                traverse(graph, neighbour, visited.copy(), path.copy(), s)


traverse(graph, 'start', visited, [], 0)

print(len(paths))
