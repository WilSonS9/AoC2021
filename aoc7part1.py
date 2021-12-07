from numpy import inf

f = list(map(int, open('./inp.txt').read().split(',')))


def checkCost(l, target, best):
    s = 0
    for e in l:
        s += abs(e-target)
        if s > best:
            return best
    return s


best = inf
for e in range(min(f), max(f)+1):
    best = checkCost(f, e, best)

print(best)
