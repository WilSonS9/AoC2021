f = open('./inp.txt').read().split('\n\n')

f1, f2 = f[0].split('\n'), f[1].split('\n')

points = {(i, j): False for i in range(15) for j in range(15)}
folds = []

xs = []
ys = []

for e in f1:
    x, y = e.split(',')
    xs.append(int(x))
    ys.append(int(y))

dims = (max(xs), max(ys))

points = {(i, j): False for i in range(
    dims[0] + 1) for j in range(dims[1] + 1)}

for e in f1:
    x, y = e.split(',')
    points[(int(x), int(y))] = True

for f in f2:
    statement = f.split('fold along ')
    folds.append(statement[1])


def fold(coords, dims, statement):
    coordX, coordY = dims
    axis, value = statement.split('=')
    value = int(value)

    if axis == 'x':
        newDims = (value, coordY)
        newCoords = {(i, j): False for i in range(value)
                     for j in range(coordY)}
        for k, v in coords.items():
            x, y = k
            if x > value:
                diff = x - value
                x2 = value - diff
                newCoords[(x2, y)] = coords[x2, y] or v

    elif axis == 'y':
        newDims = coordX, value
        newCoords = {(i, j): False for i in range(coordX)
                     for j in range(value)}
        for k, v in coords.items():
            x, y = k
            if y > value:
                diff = y - value
                y2 = value - diff
                newCoords[(x, y2)] = coords[x, y2] or v

    return (newCoords, newDims)


def printCoords(coords, dims):
    x, y = dims
    for j in range(y):
        row = ''
        for i in range(x):
            if coords[i, j]:
                row += '#'
            else:
                row += '.'
        print(row)


for folding in folds:
    points, dims = fold(points, dims, folding)

printCoords(points, dims)
