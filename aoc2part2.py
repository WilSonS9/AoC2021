f = open('./inp.txt').read().split('\n')

l = []

for e in f:
    a = e.split(' ')
    l.append((a[0], int(a[1])))


def move(d, h, aim, move, val):
    if move == 'forward':
        return (d+aim*val, h+val, aim)
    elif move == 'up':
        return (d, h, aim-val)
    elif move == 'down':
        return (d, h, aim+val)


d = 0
h = 0
aim = 0

for k in l:
    d, h, aim = move(d, h, aim, k[0], k[1])

print(d*h)
