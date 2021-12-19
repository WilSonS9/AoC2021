from functools import reduce
from itertools import combinations

f = open('inp.txt').read().split('\n\n')

scannedCoords = []


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def man(a, b):
    return sum(tuple(abs(x-y) for x, y in zip(a, b)))


def diffTable(coords):
    return {p: list(sub(p, q) for q in coords) for p in coords}


def orient(pt, orientation):
    a, b, c = pt
    return (
        (+a, +b, +c), (+b, +c, +a), (+c, +a, +
                                     b), (+c, +b, -a), (+b, +a, -c), (+a, +c, -b),
        (+a, -b, -c), (+b, -c, -a), (+c, -a, -
                                     b), (+c, -b, +a), (+b, -a, +c), (+a, -c, +b),
        (-a, +b, -c), (-b, +c, -a), (-c, +a, -
                                     b), (-c, +b, +a), (-b, +a, +c), (-a, +c, +b),
        (-a, -b, +c), (-b, -c, +a), (-c, -a, +
                                     b), (-c, -b, -a), (-b, -a, -c), (-a, -c, -b)
    )[orientation]


def allPossibleOrientations(pts):
    return [list(orient(x, i) for x in pts) for i in range(24)]


def findScannerOffset(coords1, coords2):
    diff1 = diffTable(coords1)
    for orientation in allPossibleOrientations(coords2):
        diff2 = diffTable(orientation)
        for k1, v1 in diff1.items():  # k1: the point in coords1, v1: the diffs of all points from k1
            for k2, v2 in diff2.items():  # k2: the point in coords2, v2: the diffs of all points from k2
                # If the overlap of the points is >= 12, maybe should be 13 because the lists include (0,0,0), the offset from the point itself, which we might not count
                if len(set(v1) & set(v2)) >= 12:
                    # k1 and k2 are the same points but different coordinates, return the offset between the two points which is also the offset between the scanners
                    return sub(k1, k2), orientation
    return False


def newAbs(absCoords, coords2):
    diff, coords2 = findScannerOffset(absCoords, coords2)
    for p in coords2:
        newP = add(p, diff)
        absCoords.append(newP)
    absCoords = list(set(absCoords))
    return absCoords


offsets = []


def makeWhole(absCoords, remaining):
    global offsets
    while True:
        print(len(remaining))
        r2 = remaining
        if len(remaining) == 0:
            return absCoords
        for r in remaining:
            res = findScannerOffset(absCoords, r)
            if not res == False:  # If overlaps are found
                offsets.append(res[0])
                absCoords = newAbs(absCoords, r)
                r2.remove(r)
                break
        remaining = r2


for e in f:
    scan = []
    l = e.split('\n')
    del l[0]
    for s in l:
        x, y, z = map(int, s.split(','))
        scan.append((x, y, z))
    scannedCoords.append(scan)

absCoords = scannedCoords[0]  # List of all beacons relative to Scanner 0
remaining = scannedCoords[1:]

a = makeWhole(absCoords, remaining)

combs = list(combinations(offsets, 2))

combs = list(map(lambda x: man(x[0], x[1]), combs))

print(max(combs))
