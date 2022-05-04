n = int(input())
num = list(map(int, input().split()))

result = 0

for v in num:
    cnt = 0

    if v == 1:
        continue
    
    for x in range(2, v+1):
        if v % x == 0:
            cnt += 1
    if cnt == 1:
        result += 1

print(result)