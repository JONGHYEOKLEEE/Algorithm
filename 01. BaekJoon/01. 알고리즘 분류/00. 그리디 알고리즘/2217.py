n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)

maxWeight = 0

for i in range(n):
    if rope[i] * (i+1) > maxWeight:
        maxWeight = rope[i] * (i+1)

print(maxWeight)