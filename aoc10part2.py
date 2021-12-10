import statistics

f = open('./inp.txt').read().split('\n')

openers = '([{<'
closers = ')]}>'
vals = {')': 1, ']': 2, '}': 3, '>': 4}

pairs = list(zip(openers, closers))

matches = {'(': ')', '[': ']', '{': '}', '<': '>'}

corrupteds = []

adds = []

for e in f:
    brackets = []
    add = []
    corrupt = False
    for c in e:
        if c in openers:
            brackets.append(c)
        else:
            if (brackets[-1], c) in pairs:
                brackets = brackets[:-1]
            else:
                corrupteds.append((e, c))
                corrupt = True
                break
    if not corrupt:
        for unclosed in brackets[::-1]:
            add.append(matches[unclosed])
        adds.append(add)

ss = []

for seq in adds:
    s = 0
    for c in seq:
        s *= 5
        s += vals[c]
    ss.append(s)

print(statistics.median(ss))
