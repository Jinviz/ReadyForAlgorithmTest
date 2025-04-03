T = int(input())
result = []

for _ in range(T):
  case = list(bin(int(input()))[::-1])

  for n in range(len(case)):
    if case[n] == '1':
      result.append(str(n))
  
print(' '.join(result))