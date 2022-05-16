time = int(input())
microwave = [300, 60, 10]
ans = list()

if time % microwave[2] != 0:
    print(-1)
else:
    for x in microwave:
        ans.append( time // x )
        time = time % x
    print(*ans)