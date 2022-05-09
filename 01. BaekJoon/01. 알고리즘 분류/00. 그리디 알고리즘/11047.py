n, k = input().split()
coin = list()
total = 0

for _ in range(int(n)):
    coin.append(int(input()))

price = int(k)

for _ in range(len(coin)):
    if price == 0:
        break

    selectedCoin = coin.pop()

    cnt = price // selectedCoin

    if cnt > 0:
        total += cnt
        price = price % selectedCoin

print(total)