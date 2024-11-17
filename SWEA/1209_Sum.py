T = int(input())

for test_case in range(1, T + 1):
  arr = [list(map(int, input().split())) for _ in range(100)]
  max_sum = 0
  left, right = 0, 0
  row, column = 0, 0
  for n in range(100):
    left += arr[n][n]
    right += arr[n][99-n]
    for m in range(100):
      row += arr[n][m]
      column += arr[m][n]
    
    if max(row, column) > max_sum:
      max_sum = max(row, column)
    row, column = 0, 0
  if max(left, right) > max_sum:
    max_sum = max(left, right)
  print(f'#{test_case} {max_sum}')  
