f = list(map(int, open('./inp.txt').read().split('\n')))

c = 0
for i in range(1, len(f)):
    if f[i] > f[i-1]:
        c += 1

print(c)
