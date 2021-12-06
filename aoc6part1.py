f = list(map(int, open('./inp.txt').read().split(',')))


def newGen(l):
    l = list(map(lambda x: x-1, l))
    still = list(filter(lambda x: x >= 0, l))
    new = list(filter(lambda x: x < 0, l))
    for e in new:
        still.append(6)
        still.append(8)
    return still


for i in range(80):
    f = newGen(f)

print(len(f))
