f = open('./inp.txt').read().split('\n')

l = []

for e in f:
    a = tuple(e.split(' | '))
    b = []
    for h in a:
        b.append(h.split(' '))
    l.append(tuple(b))

c = 0

for i in range(len(l)):
    for sig in l[i][1]:
        if len(sig) == 2 or len(sig) == 3 or len(sig) == 4 or len(sig) == 7:
            c += 1

print(c)
