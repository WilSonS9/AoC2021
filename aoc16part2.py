from functools import reduce

f = open('./inp.txt').read()

n = str(bin(int(f, 16)))

n = n[2:]

add = len(n) % 4

n = add*'0' + n

def explore(s, i):  # Explores the next packet
    v = int(s[i:i+3], 2)
    t = int(s[i+3:i+6], 2)
    if t == 4:
        last = False
        valString = ''
        j = i+6
        while not last:
            if s[j] == '0':
                last = True
            valString += s[j+1:j+5]
            j += 5
        val = int(valString,2)
        return (j, val)
    else:
        subVals = []
        I = s[i+6]
        if I == '0':
            i = i+7
            l = int(s[i:i+15], 2)
            i = i+15
            j = i
            while j-i < l:
                j, v = explore(s, j)
                subVals.append(v)
        elif I == '1':
            i = i+7
            l = int(s[i:i+11], 2)
            numSubs = 0
            i = i+11
            j = i
            while l - numSubs > 0:
                j, v = explore(s, j)
                numSubs += 1
                subVals.append(v)
        val = 0
        if t == 0:
            val = sum(subVals)
        elif t == 1:
            val = reduce(lambda a,b: a*b, subVals)
        elif t == 2:
            val = min(subVals)
        elif t == 3:
            val = max(subVals)
        elif t == 5:
            val = int(subVals[0] > subVals[1])
        elif t == 6:
            val = int(subVals[0] < subVals[1])
        elif t == 7:
            val = int(subVals[0] == subVals[1])
        return (j,val)


_,v = explore(n, 0)

print(v)
