f = open('./inp.txt').read().split('\n')

nums = []

for e in f:
    row = []
    for k in e:
        row.append(int(k))
    nums.append(row)


def checkMin(i, j, l):
    h = l[i][j]

    if i == len(l) - 1:
        if j == len(l[0]) - 1:
            return h < l[i-1][j] and h < l[i][j-1]
        elif j == 0:
            return h < l[i-1][j] and h < l[i][j+1]
        else:
            return h < l[i-1][j] and h < l[i][j-1] and h < l[i][j+1]

    elif i == 0:
        if j == len(l[0]) - 1:
            return h < l[i+1][j] and h < l[i][j-1]
        elif j == 0:
            return h < l[i+1][j] and h < l[i][j+1]
        else:
            return h < l[i+1][j] and h < l[i][j-1] and h < l[i][j+1]

    if j == len(l[0]) - 1:
        return h < l[i+1][j] and h < l[i-1][j] and h < l[i][j-1]
    elif j == 0:
        return h < l[i+1][j] and h < l[i-1][j] and h < l[i][j+1]

    else:
        return h < l[i+1][j] and h < l[i-1][j] and h < l[i][j+1] and h < l[i][j-1]


s = 0

for i in range(len(nums)):
    for j in range(len(nums[0])):
        if checkMin(i, j, nums):
            s += 1 + nums[i][j]

print(s)
