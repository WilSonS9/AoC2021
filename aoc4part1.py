f = open('./inp.txt').read().split('\n\n')

nums = list(map(int, f[0].split(',')))


def checkRow(board, bingoDict):
    for row in board:
        c = 0
        for i in row:
            if bingoDict[i]:
                c += 1
            else:
                break
        if c == len(row):
            return True
    return False


def checkCol(board, bingoDict):
    for j in range(len(board)):
        c = 0
        for i in range(len(board[0])):
            if bingoDict[board[i][j]]:
                c += 1
            else:
                break
        if c == len(board[0]):
            return True
    return False


def checkBingo(board, bingoDict):
    return checkRow(board, bingoDict) or checkCol(board, bingoDict)


boards = []

bingoDict = {k: 0 for k in range(100)}

for i in range(1, len(f)):
    newBoard = []
    board = f[i].split('\n')
    for row in board:
        r = list(map(int, filter(lambda x: len(x) > 0, row.split(' '))))
        newBoard.append(r)
    boards.append(newBoard)

latestNum = 0

winningBoard = []

cont = True

for num in nums:
    if cont:
        bingoDict[num] = True
        for board in boards:
            if checkBingo(board, bingoDict):
                winningBoard = board
                cont = False
                break
        latestNum = num

s = 0
for row in board:
    for col in row:
        if not bingoDict[col]:
            s += col

print(s*latestNum)
