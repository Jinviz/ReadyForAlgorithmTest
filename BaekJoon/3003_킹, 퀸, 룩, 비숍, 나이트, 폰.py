inputs = list(map(int, input().split()))
# 체스 말 규칙
chess = [1, 1, 2, 2, 2, 8]
# 필요한 말의 개수
num = [] 

for index, i in enumerate(inputs):
    if i == chess[index]:
        num.append(0)
    else:
        num.append(chess[index] - i)

for n in num:
    print(n)
        