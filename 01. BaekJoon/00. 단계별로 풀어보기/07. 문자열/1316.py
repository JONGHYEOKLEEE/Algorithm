n = int(input())
word = list()
cnt = 0

for i in range(n):
    word.append(input())

for x in word:
    arr = list(x)
    isOk = True

    for v in list(set(arr)):
        indexList = [index for index, val in enumerate(arr) if val == v]

        if len(indexList) > 1:
            if indexList[-1] - indexList[0] + 1 != len(indexList):
                isOk = False
                break
    
    if isOk == True:
        cnt += 1
        
print(cnt)