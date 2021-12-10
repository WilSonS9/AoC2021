f = open('./inp.txt').read().split('\n')

openers = '([{<'
closers = ')]}>'
vals = {')': 3, ']': 57, '}': 1197, '>': 25137}

pairs = list(zip(openers, closers))

corrupteds = []

for e in f:
    brackets = []
    for c in e:
        if c in openers:
            brackets.append(c)
        else:
            if (brackets[-1], c) in pairs:
                brackets = brackets[:-1]
            else:
                corrupteds.append((e, c))
                break

s = 0
for corrupt in corrupteds:
    s += vals[corrupt[1]]

print(s)
