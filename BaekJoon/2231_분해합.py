n = int(input())
case = []

for i in range(n):
    number = str(i)
    sum = 0
    ran = len(number)
    for j in range(ran):
        sum += int(number[j])
    if sum + i == n:
        case.append(i)

if case:
    print(min(case))
else:
    print(0)