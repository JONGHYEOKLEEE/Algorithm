# from collections import Counter

# word = input()
# cnt = Counter(word.upper())

# arr = cnt.most_common()

# if len(arr)>2 and arr[0][1] == arr[1][1]:
#     print("?")
# else:
#     print(arr[0][0])

word = input()
arr = list(map(str, word.upper()))
setArr = list(set(arr))
cntWord = list()

for x in setArr:
    cntWord.append(arr.count(x))

if cntWord.count(max(cntWord)) > 1:
    print("?")
else:
    print(setArr[cntWord.index(max(cntWord))])