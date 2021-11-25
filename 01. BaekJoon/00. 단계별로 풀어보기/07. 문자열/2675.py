t = int(input())

for i in range(t):
    a, b = input().split()
    result = ""

    for x in b:
        result += int(a)*x
    print(result)