n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

reversed_coin = reversed(coin)
count = 0
remain = k

for money in reversed_coin:
    if remain / money >= 1:
        a, b = divmod(remain, money)
        count += a
        remain = b

print(count)