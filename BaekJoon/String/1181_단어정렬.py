N = int(input())
letters = set(input() for _ in range(N))
len_case = {n: [] for n in range(1,51)}

for letter in letters:
  len_case[len(letter)].append(letter)

for i in range(1,51):
  if len(len_case[i]) > 0:
    len_case[i].sort()
    for j in len_case[i]:
      print(j)