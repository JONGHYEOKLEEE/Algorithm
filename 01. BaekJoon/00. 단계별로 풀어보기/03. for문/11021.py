import sys
input = lambda:sys.stdin.readline().rstrip()

t = int(input())
x = list()

for i in range(t):
    a, b = map(int, input().split())
    x.append(a+b)

for i in range(1, t+1):
    print("Case #%d:" %i, x[i-1], sep=" ")