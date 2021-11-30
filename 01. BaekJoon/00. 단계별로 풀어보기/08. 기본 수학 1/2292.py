n = int(input())
honeyComb = 1
cnt = 1

while n > honeyComb:
    honeyComb += cnt * 6
    cnt += 1
    
print(cnt)