n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = list()

for v in arr:
    if v<x:
        result.append(v)
        
for i in result:
    print(i, end=" ")