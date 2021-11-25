def hansu(n):
    cnt = 0

    for i in range(1, n+1):
        arr = list(map(int, str(i)))

        if len(arr)<3:
            cnt += 1
        else:
            diff = arr[0]-arr[1]

            for j in range(1, len(arr)):
                if j == len(arr)-1:
                    cnt += 1
                    break

                x = arr[j]-arr[j+1]

                if x != diff:
                    break
    print(cnt)

hansu(int(input()))