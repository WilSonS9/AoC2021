import networkx as nx

G = nx.DiGraph()


def addWrapAround(n, a):
    if not n+a >= 10:
        return n+a
    else:
        return n - 9 + a


f = open('./inp.txt').read().split('\n')

xMax = len(f[0])
yMax = len(f)

# (y,x) coords for some reason

nodes = [(i, j) for j in range(5*xMax) for i in range(5*yMax)]

for i in range(5*yMax):
    for j in range(5*xMax):
        coord = (i, j)
        tmp = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        if i == 0:
            tmp.remove((i-1, j))
        elif i == 5*yMax - 1:
            tmp.remove((i+1, j))
        if j == 0:
            tmp.remove((i, j-1))
        elif j == 5*xMax - 1:
            tmp.remove((i, j+1))
        for i, j in tmp:
            xGen = j // xMax
            orgX = j % xMax
            yGen = i // yMax
            orgY = i % yMax
            add = xGen + yGen
            orgWeight = int(f[orgY][orgX])
            weight = addWrapAround(orgWeight, add)
            G.add_edge(coord, (i, j), weight=weight)
print(G)
source = (0, 0)
target = (5*yMax-1, 5*xMax-1)

path = nx.shortest_path_length(
    G, source=source, target=target, weight='weight')

print(path)
