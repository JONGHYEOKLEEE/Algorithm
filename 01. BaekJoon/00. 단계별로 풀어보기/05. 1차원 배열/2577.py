arr = list()

for i in range(3):
    arr.append(int(input()))

v = arr[0]*arr[1]*arr[2]
result = list(map(int, str(v)))

for i in range(10):
    print(result.count(i))