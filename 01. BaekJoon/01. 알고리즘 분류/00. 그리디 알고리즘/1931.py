import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
classTime = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))
ans = end = 0

for startTime, endTime in classTime:
    if startTime >= end:
        ans += 1
        end = endTime

print(ans)