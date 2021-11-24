remain = list()
cnt = 0

for i in range(10):
    remain.append(int(input())%42)

result = set(remain)

print(len(result))