n = int(input())
arr = list(map(int, input().split()))
result = list()
m = max(arr)

for v in arr:
    result.append(v/m*100)

total = sum(result)
avg = total/len(result)

print(avg)