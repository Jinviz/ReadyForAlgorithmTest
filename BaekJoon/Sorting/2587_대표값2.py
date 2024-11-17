number = [int(input()) for _ in range(5)]

number.sort()
sum = 0
for i in range(5):
  sum += number[i]

average = sum // 5

print(average)
print(number[2])