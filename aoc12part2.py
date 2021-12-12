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


def traverse(graph, node, visited, path, s, small, cb):
    global paths
    if not visited[node]:
        s += 1
        path.append(node)
        capsOrNot = [True if c in caps else False for c in node]
        if not all(capsOrNot):
            if not node == small:
                visited[node] = True
            elif node == small and not cb:
                cb = True
            elif node == small and cb:
                visited[node] = True
        if node == 'end':
            if not path in paths:
                paths.append(path)
        else:
            neighbours = graph[node]
            for neighbour in neighbours:
                # print(node, path, visited, s)
                traverse(graph, neighbour, visited.copy(),
                         path.copy(), s, small, cb)


smalls = []

for node in graph.keys():
    capsOrNot = [True if c in caps else False for c in node]
    if not all(capsOrNot) and not node in ['start', 'end']:
        smalls.append(node)

print(smalls)

for node in smalls:
    print(node)
    traverse(graph, 'start', visited.copy(), [], 0, node, False)

print(len(paths))
