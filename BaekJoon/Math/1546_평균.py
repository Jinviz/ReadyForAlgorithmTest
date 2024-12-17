N = int(input())

score = list(map(int, input().split()))
max_score = max(score)
new_score = []

for n in range(N):
  new_score.append(score[n]/max_score*100)

print(sum(new_score)/N)