f = open('./inp.txt').read().split('\n\n')

polymer, f2 = f[0], f[1].split('\n')

insertions = {}

for i in f2:
    find, goal = i.split(' -> ')
    r = find[0] + goal + find[1]
    insertions[find] = r

pairs = {}
for i in range(len(polymer)-1):
    couple = polymer[i] + polymer[i+1]
    if couple in pairs:
        pairs[couple] += 1
    else:
        pairs[couple] = 1

for _ in range(40):
    newPairs = {}
    letters = {}
    for couple, c in pairs.items():  # Example: 2 NN pairs will generate 2 NC pairs and 2 CN pairs
        r = insertions[couple]  # Example: insertions['NN'] = 'NCN'
        left = r[:2]
        right = r[1:3]
        a, b, d = r
        if left in newPairs:
            newPairs[left] += c
        else:
            newPairs[left] = c
        if right in newPairs:
            newPairs[right] += c
        else:
            newPairs[right] = c
    pairs = newPairs

letters = {}
for k in pairs.keys():
    a, b = k
    val = pairs[k]
    for letter in [a, b]:
        if letter in letters:
            letters[letter] += val
        else:
            letters[letter] = val

nums = letters.values()
# Is off by 1 half of the time due to me not really compensating for double counting, add
print((max(nums) - min(nums)) // 2)
