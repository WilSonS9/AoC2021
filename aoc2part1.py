f = open('./inp.txt').read().split('\n')

l = []

for e in f:
    a = e.split(' ')
    l.append((a[0], int(a[1])))


def move(d, h, move, val):
    if move == 'forward':
        return (d, h+val)
    elif move == 'up':
        return (d-val, h)
    elif move == 'down':
        return (d+val, h)


d = 0
h = 0

for k in l:
    d, h = move(d, h, k[0], k[1])

print(d*h)
