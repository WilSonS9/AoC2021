import networkx as nx

G = nx.DiGraph()

f = open('./inp.txt').read().split('\n')

xMax = len(f[0])
yMax = len(f)

# (y,x) coords for some reason

nodes = [(i, j) for j in range(xMax) for i in range(yMax)]

for i in range(yMax):
    for j in range(xMax):
        coord = (i, j)
        tmp = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        neighbours = {}
        if i == 0:
            tmp.remove((i-1, j))
        elif i == yMax - 1:
            tmp.remove((i+1, j))
        if j == 0:
            tmp.remove((i, j-1))
        elif j == xMax - 1:
            tmp.remove((i, j+1))
        for i, j in tmp:
            G.add_edge(coord, (i, j), weight=int(f[i][j]))
print(G)
source = (0, 0)
target = (yMax-1, xMax-1)

path = nx.shortest_path_length(
    G, source=source, target=target, weight='weight')

print(path)
