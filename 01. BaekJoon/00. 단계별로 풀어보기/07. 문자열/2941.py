alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for x in alpha:
    word = word.replace(x, '*')

print(len(word))