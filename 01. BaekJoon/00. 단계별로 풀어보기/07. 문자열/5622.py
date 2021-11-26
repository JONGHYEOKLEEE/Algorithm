num = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
tel = list(input())
time = 0

for v in tel:
    for index, x in enumerate(num):
        if v in x:
            time += index + 3
    
print(time)