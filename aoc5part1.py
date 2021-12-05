f = open('./inp.txt').read().split('\n')

l = []

for e in f:
    pairs = e.split(' -> ')
    start = tuple(map(int, pairs[0].split(',')))
    stop = tuple(map(int, pairs[1].split(',')))
    if start[0] == stop[0] or start[1] == stop[1]:
        l.append((start, stop))

coords = {(x, y): 0 for y in range(1000) for x in range(1000)}

for pair in l:
    start, stop = pair
    if start[0] > stop[0] or start[1] > stop[1]:
        start, stop = stop, start
    allCoords = [(x, y) for y in range(start[1], stop[1]+1)
                 for x in range(start[0], stop[0]+1)]
    for coord in allCoords:
        coords[coord] += 1

c = 0

coordList = [(x, y) for y in range(1000) for x in range(1000)]

for coord in coordList:
    if coords[coord] >= 2:
        c += 1

print(c)
