n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = 0

if len(set(cost)) == 1 and set(cost).pop() == 1:
    print(sum(road))
else:
    for i in range(n-1):
        ans += road[i] * cost[i]
        
        if cost[i] <= cost[i+1]:
            cost[i+1] = cost[i]

    print(ans)