## 시도(1)
# import sys

# N = int(input())
# number = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# number.sort()
# print("----")
# for i in range(N):
#   print(number[i])

## 시도(2)
# import sys

# N = int(input())
# number = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# for i in range(N):
#   print(min(number))
#   index = number.index(min(number))
#   number.pop(index)

## 계수 정렬을 이용
import sys

N = int(input())

arr = [0] * 10001
for _ in range(N):
  m = int(sys.stdin.readline().rstrip())
  arr[m] += 1

for i in range(10001):
  if arr[i] != 0:
    for _ in range(arr[i]):
      print(i)