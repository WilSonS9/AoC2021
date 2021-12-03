f = open('./inp.txt').read().split('\n')


# cB (coolBool) decides whether or not we are looking for the O2 or the CO2 number
def coolFilterStuff(f, cB):
    num = 0
    for n in range(len(f[0])):
        oneC = 0
        zeroC = 0
        for i in f:
            if i[n] == '1':
                oneC += 1
            else:
                zeroC += 1
        if len(f) == 1:
            num = int(f[0], 2)
            return num
        else:
            if oneC >= zeroC:
                f = list(filter(lambda x: x[n] == str(int(cB)), f))
            else:
                f = list(filter(lambda x: x[n] == str(int(not cB)), f))
            if len(f) == 1:
                num = int(f[0], 2)
                return num


print(coolFilterStuff(f, 1) * coolFilterStuff(f, 0))
