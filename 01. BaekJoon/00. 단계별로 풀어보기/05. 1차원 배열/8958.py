n = int(input())

for i in range(n):
    ox = input()
    arr = list(ox)

    total = 0
    up = 1

    for x in arr:
        if x == "O":
            total += up
            up += 1
        else:
            up = 1
    print(total)