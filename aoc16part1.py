f = open('./inp.txt').read()

n = str(bin(int(f, 16)))

n = n[2:]

add = len(n) % 4

n = add*'0' + n

versionSum = 0


def explore(s, i):  # Explores the next packet
    global versionSum
    v = int(s[i:i+3], 2)
    versionSum += v
    t = int(s[i+3:i+6], 2)
    if t == 4:
        last = False
        j = i+6
        while not last:
            if s[j] == '0':
                last = True
            j += 5
        return j
    else:
        I = s[i+6]
        if I == '0':
            i = i+7
            l = int(s[i:i+15], 2)
            i = i+15
            j = i
            while j-i < l:
                j = explore(s, j)
            return j
        elif I == '1':
            i = i+7
            l = int(s[i:i+11], 2)
            numSubs = 0
            i = i+11
            j = i
            while l - numSubs > 0:
                j = explore(s, j)
                numSubs += 1
            return j


explore(n, 0)

print(versionSum)
