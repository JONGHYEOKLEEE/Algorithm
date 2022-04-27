h, m = map(int, input().split())
time = int(input())

sumMin = m + time

if sumMin >= 60:
    h += sumMin // 60

    h %= 24
    sumMin %= 60

print(h, sumMin)