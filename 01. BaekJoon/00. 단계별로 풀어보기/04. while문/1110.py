from collections import deque

n = int(input())
arr = deque(map(int, str(n)))

if n<10:
    arr.appendleft(0)

v = cnt = 0

while True:
    x = 0
    
    for i in range(len(arr)):
        x += arr[i]
    
    tmp = list(map(int, str(x)))
    
    arr.popleft()
    arr.append(tmp[-1])
    
    cnt += 1
    v = int(''.join(map(str, arr)))

    if v==n:
        print(cnt)
        break