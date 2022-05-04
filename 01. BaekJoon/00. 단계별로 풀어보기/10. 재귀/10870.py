# 이게 왜 안돼?
# n = int(input())

# fibo = [0, 1]

# for _ in range(0, n-1):
#     num = fibo[0] + fibo[1]
#     fibo[0], fibo[1] = fibo[1], num

# print(fibo[1])

# 인터넷 출처 풀이

n = int(input())

def fibo(num):
    if num<=1:
        return num
    return fibo(num-1) + fibo(num-2)

print(fibo(n))