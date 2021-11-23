a = int(input())
arr = list(map(int, input()))
b = int(''.join(map(str, arr)))

print(a*arr[2], a*arr[1], a*arr[0], a*b, sep='\n')