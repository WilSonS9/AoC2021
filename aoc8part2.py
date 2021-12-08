from itertools import permutations

f = open('./inp.txt').read().split('\n')

l = []

keyDict = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4,
           'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}

allPerms = list(permutations('abcdefg'))

for e in f:
    a = tuple(e.split(' | '))
    b = []
    for h in a:
        b.append(h.split(' '))
    l.append(tuple(b))

s = 0

for p1 in allPerms:
    p = ''.join(p1)
    mapping = dict(zip('abcdefg', p))
    for i in l:
        j = set()
        for k1 in i:
            for k in k1:
                jk = []
                for c in k:
                    jk.append(mapping[c])
                res = ''.join(jk)
                j.add((''.join(sorted(res)), res, k))
        digs = {key[2]: 0 for key in j}
        cont = True
        for e in j:
            try:
                digs[e[2]] = keyDict[e[0]]
            except:
                cont = False
                break
        if cont:
            print(digs)
            coolList = []
            for out in i[1]:
                coolList.append(str(digs[out]))
            add = int(''.join(coolList))
            print(add)
            s += add

print(s)
