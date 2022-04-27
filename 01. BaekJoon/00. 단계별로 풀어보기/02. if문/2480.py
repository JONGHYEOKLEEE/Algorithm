dice = list(map(int, input().split()))
cntOfSameNum = list()

for v in dice:
    cntOfSameNum.append(dice.count(v))

maxCnt = max(cntOfSameNum)

if maxCnt == 3:
    total = 10000 + dice[cntOfSameNum.index(maxCnt)] * 1000
    print(total)
elif maxCnt == 2:
    total = 1000 + dice[cntOfSameNum.index(maxCnt)] * 100
    print(total)
elif maxCnt == 1:
    total = 100 * max(dice)
    print(total)