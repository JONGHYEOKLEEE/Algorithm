t = int(input())
arr = list()

for i in range(t):
    a, b = map(int, input().split())

    arr.append(a+b)
    
for i in arr:
    print(i)