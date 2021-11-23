x = int(input())
y = int(input())

print(1 if 0<x and 0<y else 2 if x<0 and 0<y else 3 if x<0 and y<0 else 4)