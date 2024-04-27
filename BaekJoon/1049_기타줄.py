N, M = map(int, input().split())
cost = [tuple(map(int, input().split())) for _ in range(M)]

# 패키지의 최소 가격과 낱개 최소 가격의 6개 가격 중 어느 가격이 더 저렴한지

sort_package = sorted(cost)
sort_one = sorted(cost, key = lambda x: x[1])

min_buying = sort_package[0][0] if sort_package[0][0] <= sort_one[0][1] * 6 else sort_one[0][1] * 6

quotient, remainder = divmod(N, 6)

result = quotient * min_buying

if remainder * sort_one[0][1] <= min_buying:
    remain_cost = remainder * sort_one[0][1]
else:
    remain_cost = min_buying

result += remain_cost
print(result)