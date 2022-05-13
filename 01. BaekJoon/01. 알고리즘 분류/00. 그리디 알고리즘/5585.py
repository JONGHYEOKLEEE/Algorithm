paid = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
ans = 0

for m in money:
    if paid >= m:
        ans += paid // m
        paid = paid % m

print(ans)