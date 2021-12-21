from collections import Counter, defaultdict

dice = list(Counter(  # All possible outcomes and how many there are of rolling 3 3-sided dirac die
                      # For example: 1 way to reach 3, 3 ways to reach 4, etc.
    i + j + k
    for i in range(1, 4)
    for j in range(1, 4)
    for k in range(1, 4)
).items())

# Format: Score 1, Pos 1, Score 2, Pos 2. Enter your own input values for Pos 1 and Pos 2
states = {(0, 6, 0, 1): 1}
p1Wins = 0
p2Wins = 0
while True:
    newStates = defaultdict(int)
    # Value: how many universes with this state there are
    for state, value in list(states.items()):
        score1, pos1, score2, pos2 = state
        for d, dcount in dice:  # dcount: how many ways of rolling this value there are, each will generate a new universe
            p1 = (pos1 + d - 1) % 10 + 1
            s1 = score1 + p1
            if s1 >= 21:
                p1Wins += value * dcount
                continue
            for d2, d2count in dice:
                p2 = (pos2 + d2 - 1) % 10 + 1
                s2 = score2 + p2
                if s2 >= 21:
                    p2Wins += value * dcount * d2count
                    continue
                newStates[(s1, p1, s2, p2)] += value * dcount * d2count
    states = newStates
    if len(states.keys()) == 0:
        break

print(max([p1Wins, p2Wins]))
