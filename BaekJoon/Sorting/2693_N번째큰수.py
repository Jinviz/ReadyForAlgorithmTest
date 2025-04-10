T = int(input())

for _ in range(T):
  case = list(map(int,input().split()))
  case.sort()

  print(case[7])