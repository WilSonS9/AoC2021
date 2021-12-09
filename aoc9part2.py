f = open('./inp.txt').read().split('\n')

nums = []

for e in f:
    row = []
    for k in e:
        if k == '9':
            row.append(1)
        else:
            row.append(0)
    nums.append(row)


def canEnter(matrix, visited, row, col):
    nRows = len(matrix)
    nCols = len(matrix[0])

    if (row < 0 or row >= nRows
        or col < 0 or col >= nCols
        or visited[row][col]
            or matrix[row][col] == 1):
        return False

    return True


sizeOut = 0


def expand(matrix, visited, row, col):
    global sizeOut

    visited[row][col] = 1
    sizeOut += 1

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not i == j and not i == -j:
                is_safe_cell = canEnter(matrix, visited, row+i,
                                        col+j)

                if (is_safe_cell):
                    expand(matrix, visited, row+i, col+j)


sizes = []


def find_islands(matrix):
    global sizeOut
    nRows = len(matrix)
    nCols = len(matrix[0])
    visited = [[0 for _ in range(nCols)] for _ in range(nRows)]

    count = 0
    for i in range(0, nRows):
        for j in range(0, nCols):
            if (matrix[i][j] == 0 and not visited[i][j]):
                sizeOut = 0
                # print('New Island Found!')

                expand(matrix, visited, i, j)

                # print('Island Size:', sizeOut)
                sizes.append(sizeOut)
                count += 1

    return count


find_islands(nums)

sizes = list(sorted(sizes, reverse=True))

print(sizes[0]*sizes[1]*sizes[2])
