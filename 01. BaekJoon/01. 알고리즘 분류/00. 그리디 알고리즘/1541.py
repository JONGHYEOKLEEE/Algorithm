val = input().split("-")
ans = 0

if len(val) > 1:
    for i in range(len(val)):
        if i == 0 and "+" not in val[i]:
            ans += int(val[i])
        elif i == 0 and "+" in val[i]:
            num = sum(list(map(int, val[i].split("+"))))
            ans += num
        elif "+" in val[i]:
            num = sum(list(map(int, val[i].split("+"))))
            ans -= num
        else:
            ans -= int(val[i])
    print(ans)
elif len(val) == 1 and "+" in val[0]:
    ans = sum(map(int, val[0].split("+")))
    print(ans)
else:
    print(val[0])