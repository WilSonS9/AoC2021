f = open('inp.txt').read().split('\n')

coords = {}
height = len(f)
width = len(f[0])

# (y,x) coords
for i in range(height):
    for j in range(width):
        c = f[i][j]
        if c in ['v','>']:
            coords[(i,j)] = c

def makeMove(coords,width,height):
    new = {}
    for k,v in coords.items():
        if v == '>':
            dest = (k[0], (k[1] + 1) % width)
            if not dest in coords.keys():
                new[dest] = v
            else:
                new[k] = v
    for k,v in coords.items():
        if v == 'v':
            dest = ((k[0] + 1) % height, k[1])
            if not dest in new.keys():
                if dest in coords.keys():
                    if not coords[dest] == v:
                        new[dest] = v
                    else:
                        new[k] = v
                else:
                    new[dest] = v
            else:
                new[k] = v
    return (new, new == coords)

def pprint(coords,width,height): # For debugging
    for i in range(height):
        row = ''
        for j in range(width):
            if (i,j) in coords.keys():
                row += coords[(i,j)]
            else:
                row += '.'
        print(row)

s = 0

while True:
    coords, stop = makeMove(coords,width,height)
    if not stop:
        s += 1
    else:
        print(s+1)
        break