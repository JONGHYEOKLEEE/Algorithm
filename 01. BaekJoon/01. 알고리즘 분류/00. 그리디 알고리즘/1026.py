import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
numListA = list(map(int, input().split()))
numListB = list(map(int, input().split()))

newNumListA = [0 for _ in range(n)]
newNumListB = numListB.copy()

ans = 0

for _ in range(n):
    minIDX, minNum = numListA.index(min(numListA)), numListA.pop(numListA.index(min(numListA)))
    maxIDX, maxNum = numListB.index(max(newNumListB)), newNumListB.pop(newNumListB.index(max(newNumListB)))

    ans += minNum * maxNum 
    #print('maxIDX : ', maxIDX)
    newNumListA[maxIDX] = minNum
    #print(newNumListA)

#print('result : ', newNumListA)

print(ans)