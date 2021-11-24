import sys
input = lambda:sys.stdin.readline().rstrip()

t = int(input())
a = list()
b = list()

for i in range(t):
    x, y = map(int, input().split())
    
    a.append(x)
    b.append(y)

for i in range(1, t+1):
    print("Case #{0}: {1} + {2} = {3}".format(i, a[i-1], b[i-1], a[i-1]+b[i-1]))