arr = list()
remain = list()
cnt = 0

for i in range(10):
    arr.append(int(input()))
    remain.append(arr[i]%42)

result = set(remain)

print(len(result))