f = open('inp.txt').read().split('\n')

space = {}

instructions = []

for e in f:
    t = e.split(' ')
    on = t[0] == 'on'
    coords = t[1].split(',')
    vals = []
    for coord in coords:
        a = coord.split('=')
        minCoord, maxCoord = map(int, a[1].split('..'))
        vals.append((minCoord, maxCoord))
    instructions.append((vals, on))

coolRange = range(-50, 51)

for instruction in instructions:
    coords, on = instruction
    x, y, z = coords
    xMin, xMax = x
    yMin, yMax = y
    zMin, zMax = z
    if xMin in coolRange and xMax in coolRange and yMin in coolRange and yMax in coolRange and zMin in coolRange and zMax in coolRange:
        for x in range(xMin, xMax+1):
            for y in range(yMin, yMax+1):
                for z in range(zMin, zMax+1):
                    coord = (x, y, z)
                    if on:
                        space[coord] = True
                    else:
                        # Deletes it from space if found, else it does nothing
                        space.pop(coord, None)

print(len(space))
