f = open('./inp.txt').read().split('\n')

coords = {}

for i in range(len(f)):
    for j in range(len(f)):
        coords[(i, j)] = int(f[i][j])


def step(coords, flashes):
    newFlashes = flashes

    def increaseNeighbours(coords, point, flashed):
        newCoords = coords
        newFlashed = flashed
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i, j) == (0, 0):
                    pointCoords = (point[0] + i, point[1] + j)
                    if 0 <= pointCoords[0] <= 9 and 0 <= pointCoords[1] <= 9:
                        newCoords[pointCoords] += 1
        return newCoords, newFlashed

    flashed = {k: False for k, _ in coords.items()}
    coords = {k: 1+v for k, v in coords.items()}

    def printSpace(coords):  # For debugging
        for i in range(10):
            row = ''
            for j in range(10):
                row += str(coords[(i, j)])
                row += ' '
            print(row)

    def checkFlash(coords, flashed, flashes):
        newCoords, newFlashed, newFlashes = coords, flashed, flashes
        for i in range(10):
            for j in range(10):
                point = (i, j)
                if coords[point] > 9 and not flashed[point]:
                    newCoords, newFlashed = increaseNeighbours(
                        coords, point, flashed)
                    newFlashes += 1
                    newFlashed[point] = True
                    return newCoords, newFlashed, True, newFlashes
        return newCoords, newFlashed, False, newFlashes

    cont = True
    while cont:
        coords, flashed, cont, newFlashes = checkFlash(
            coords, flashed, newFlashes)

    for k, v in flashed.items():
        if v:
            coords[k] = 0

    return coords, newFlashes


flashes = 0

for _ in range(100):
    coords, flashes = step(coords, flashes)

print(flashes)
