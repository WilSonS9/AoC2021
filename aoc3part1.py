f = open('./inp.txt').read().split('\n')

d = ''
e = ''

for n in range(len(f[0])):
    oneC = 0
    zeroC = 0
    for i in f:
        if i[n] == '1':
            oneC += 1
        else:
            zeroC += 1
    d += str(int(oneC > zeroC))
    e += str(int(not oneC > zeroC))

print(int(d, 2) * int(e, 2))
