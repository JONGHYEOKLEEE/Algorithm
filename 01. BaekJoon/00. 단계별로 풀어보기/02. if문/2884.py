h, m = map(int, input().split())

if m>=45:
    print(h, m-45, sep=(" "))
else:
    if h<1:
        print(h+23, m+15, sep=(" "))
    else:
        print(h-1, m+15, sep=(" "))