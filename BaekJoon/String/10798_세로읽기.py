line = []
max = 0 
result = ''
for _ in range(5):
  line.append(input())
  if len(line[-1]) > max: 
    max = len(line[-1])  

for n in range(max):
    for m in range(5):
      if len(line[m]) > n:
        result += line[m][n]

print(result)