T = int(input())
for test_case in range(1, T+1):
  arr = []
  length, palin, side = 0,0,0
  N, M = map(int, input().split())
  for n in range(N):
    string = input()
    if string[::-1] in arr:
      side += 2
    if string == string[::-1]:
      palin = M
    arr.append(string)

  length = (M * side) + palin
  print(f'#{test_case} {length}')