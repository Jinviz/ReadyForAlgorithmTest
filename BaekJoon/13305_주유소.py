N = int(input())    # 도시의 개수
km = list(map(int, input().split()))    # 도시 간 거리
oil_price = list(map(int, input().split()))
oil_price.pop()
# 첫 출발은 무조건 주유를 하긴 해야 함
# n번 주유소가 가장 싸면 이후 남은 거리 모두 주유(마지막 도시 제외)
# n번 주유소에서 남은 주유소 가격 중 n번보다 싼 도시까지 거리를 주유
sum_price = 0

for n in range(N-1):
    if oil_price[n] == min(oil_price):
        for i in range(n, N-1):
            sum_price += km[i] * oil_price[n]
        break

    else:
        for until in range(n+1, N-1):
            if oil_price[until] < oil_price[n]:
                for i in range(n, until):
                    sum_price += km[i] * oil_price[n]
                    km[i] = 0
                break

print(sum_price)