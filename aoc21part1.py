p1 = 5
s1 = 0
p2 = 0
s2 = 0
diceVal = 1
diceNum = 0

board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    p1 = p1 + 3*(diceVal+1)
    p1 = board[p1 % 10]
    diceNum += 3
    diceVal += 3
    s1 += p1
    p1 -= 1

    if s1 >= 1000:
        loser = s2
        print(loser*diceNum)
        break

    p2 = p2 + 3*(diceVal+1)
    p2 = board[p2 % 10]
    diceNum += 3
    diceVal += 3
    s2 += p2
    p2 -= 1

    if s2 >= 1000:
        loser = s1
        print(loser*diceNum)
        break
