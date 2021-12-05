f = open('./inp.txt').read().split('\n')

l = []

for e in f:
    pairs = e.split(' -> ')
    start = tuple(map(int, pairs[0].split(',')))
    stop = tuple(map(int, pairs[1].split(',')))
    if start[0] == stop[0] or start[1] == stop[1] or abs(start[0] - stop[0]) == abs(start[1] - stop[1]):
        l.append((start, stop))

coords = {(x, y): 0 for y in range(1000) for x in range(1000)}

for pair in l:
    start, stop = pair
    if start[0] == stop[0] or start[1] == stop[1]:
        if start[0] > stop[0] or start[1] > stop[1]:
            start, stop = stop, start
        allCoords = [(x, y) for y in range(start[1], stop[1]+1)
                     for x in range(start[0], stop[0]+1)]
    else:
        revX = False
        revY = False
        x1, y1 = start
        x2, y2 = stop
        if x1 > x2:
            x1, x2 = x2, x1
            revX = True
        allX = [x for x in range(x1, x2 + 1)]
        if revX:
            allX = allX[::-1]
        if y1 > y2:
            y1, y2 = y2, y1
            revY = True
        allY = [y for y in range(y1, y2 + 1)]
        if revY:
            allY = allY[::-1]
        allCoords = list(zip(allX, allY))
    for coord in allCoords:
        coords[coord] += 1

c = 0

coordList = [(x, y) for y in range(1000) for x in range(1000)]

for coord in coordList:
    if coords[coord] >= 2:
        c += 1

print(c)
