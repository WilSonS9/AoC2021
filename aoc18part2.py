from math import ceil
from functools import reduce
from itertools import permutations

f = open('inp.txt').read().split('\n')


def build(inp):  # Make a flattened list!
    out = []
    level = 0
    for c in inp:
        if c in '[]':
            level += 1 if c == '[' else -1
        elif c != ',':
            out.append((int(c), level))
    return out


def explode(n):  # Finds first pair with depth >= 4, explodes it, returns True if it has exploded, False otherwise
    for i in range(len(n)):
        lValue, depth = n[i]
        if depth >= 5:
            l, r = n[i], n[i+1]
            rValue = r[0]
            if i > 0:
                n[i-1] = (n[i-1][0] + lValue, n[i-1][1])
            if i+2 < len(n):
                n[i+2] = (n[i+2][0] + rValue, n[i+2][1])
            n[i:i+2] = [(0, depth-1)]
            return True
    return False


def split(n):
    for i in range(len(n)):
        value, depth = n[i]
        if value >= 10:
            # This splicing can extend the flattened list
            n[i:i+1] = (value//2, depth+1), (ceil(value/2), depth+1)
            return True
    return False


def add(l, r):
    n = list(map(lambda x: (x[0], x[1] + 1), l + r))
    while True:
        if not explode(n):
            if not split(n):
                return n


def magnitude(t):
    n = t
    while True:
        for i in range(len(n)-1):
            if n[i][1] == n[i+1][1]:  # If the depths are equal
                # Replaces the pair elements with 1 element equivalent to the magnitude of these numbers, reduce the depth as we are going one level up:
                # For example, [(1,2), (2,2), (5,1)] first becomes [(7,1), (5,1)] and then [(31, 0)]
                # We are recursing 'backwards'
                n[i:i+2] = [(3*n[i][0]+2*n[i+1][0], n[i][1]-1)]
                break
        else:
            break
    return n[0][0]


f = list(map(build, f))

f = list(permutations(f, 2))

mags = []

for e in f:
    n = reduce(add, e)
    mags.append(magnitude(n))

print(max(mags))
