a, b = input().split()

arr1 = list(a)
arr2 = list(b)

arr1.reverse()
arr2.reverse()

a = ''.join(arr1)
b = ''.join(arr2)

print(a) if a>b else print(b)