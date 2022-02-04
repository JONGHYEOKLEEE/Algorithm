n = int(input())

for i in range(n):
    H, W, N = map(int, input().split())
    
    if N%H == 0:
        num = N//H
        floor = H
    else:
        num = N//H + 1
        floor = N%H
        
    print(f'{floor*100+num}')