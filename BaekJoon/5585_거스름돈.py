money = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
sum = 0
for n in range(6):
    dump_sum, money = divmod(money, coin[n])
    sum += dump_sum

print(sum) 