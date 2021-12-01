f = list(map(int, open('./inp.txt').read().split('\n')))

sums = []

c = 0
for i in range(1, len(f)):
    try:
        sums.append(f[i] + f[i+1] + f[i+2])
    except:
        break

for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        c += 1

print(c)
