from collections import deque

c = int(input())

for i in range(c):
    a = deque(map(int, input().split()))
    
    n = a.popleft()
    avg = sum(a)/n

    cnt = 0

    for x in a:
        if x>avg:
            cnt += 1
    
    print(f"{(cnt/n)*100:.3f}%")