# ** 수정해야함 **

money = int(input())
price = list(map(int, input().split()))

# 준헌(BNP) 방식
junheon_stock = money // price[0]  # 초기 주식 수
junheon_money = money % price[0]   # 남은 돈
junheon_money += junheon_stock * price[-1]  # 마지막에 주식 전량 매도

# 성민(TIMING) 방식
sungmin_money = money
sungmin_stock = 0
continuous_up = 0
continuous_down = 0

for i in range(1, len(price)):
    if price[i] > price[i-1]:
        continuous_up += 1
        continuous_down = 0  # 상승 시 하락 연속 카운트 초기화
    elif price[i] < price[i-1]:
        continuous_down += 1
        continuous_up = 0  # 하락 시 상승 연속 카운트 초기화
    else:
        continuous_up = 0
        continuous_down = 0

    # 성민이 주식을 파는 경우 (3일 연속 상승)
    if continuous_up >= 3 and sungmin_stock > 0:
        sungmin_money += sungmin_stock * price[i]
        sungmin_stock = 0
    # 성민이 주식을 사는 경우 (3일 연속 하락)
    elif continuous_down >= 3:
        stocks_to_buy = sungmin_money // price[i]
        sungmin_stock += stocks_to_buy
        sungmin_money -= stocks_to_buy * price[i]

# 마지막에 성민도 남은 주식 매도
sungmin_money += sungmin_stock * price[-1]

# 결과 비교
if sungmin_money > junheon_money:
    print("TIMING")
elif junheon_money > sungmin_money:
    print("BNP")
else:
    print("SAMESAME")
