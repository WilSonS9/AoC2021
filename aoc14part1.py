f = open('./inp.txt').read().split('\n\n')

polymer, f2 = f[0], f[1].split('\n')

insertions = {}

for i in f2:
    find, goal = i.split(' -> ')
    r = find[0] + goal + find[1]
    insertions[find] = r


def step(polymer, insertions):
    newPolymer = ''
    for i in range(len(polymer) - 1):
        i, j = i, i+1
        pair = polymer[i] + polymer[j]
        add = ''
        if pair in insertions.keys():
            add = insertions[pair][:2]
        else:
            add = polymer[i]
        if j == len(polymer) - 1:
            add += polymer[j]
        newPolymer += add
    return newPolymer


for _ in range(10):
    polymer = step(polymer, insertions)

freqs = [polymer.count(e) for e in set(polymer)]

print(max(freqs) - min(freqs))
