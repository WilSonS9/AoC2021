from typing import ForwardRef


f = list(map(int, open('./inp.txt').read().split(',')))

nums = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

for e in f:
    nums[e] += 1


def newGen(nums):
    newNums = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for key in nums:
        val = nums[key]
        if not key == 0:
            newNums[key-1] += val
        else:
            newNums[6] += val
            newNums[8] += val
    return newNums


for _ in range(256):
    nums = newGen(nums)

s = 0

for key in nums:
    s += nums[key]

print(s)
