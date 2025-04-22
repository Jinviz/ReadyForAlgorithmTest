N, M = map(int,input().split())

matrix_n, matrix_m = [],[]

for _ in range(N):
  matrix_n.append(list(map(int,input().split())))

for _ in range(N):
  matrix_m.append(list(map(int,input().split())))
  
for i in range(N):
  temp = []
  for j in range(M):
    temp.append(str(matrix_n[i][j] + matrix_m[i][j]))
  print(' '.join(temp))