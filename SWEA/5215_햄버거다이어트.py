# T = int(input())
# for test_case in range(1, T+1):
#   M, max_calorie = map(int, input().split())
#   score, calorie = [], []

#   for _ in range(M):
#     a, b = map(int, input().split())
#     score.append(a)
#     calorie.append(b)

#   result = 0
#   def combine_material(index, current_score, current_calorie):
#     global result
#     if index == M:
#       return
#     for m in range(index, M):
#       if current_calorie + calorie[m] <= max_calorie:
#         current_calorie += calorie[m]
#         current_score += score[m]
#         if current_score > result: 
#           result = current_score 
#     combine_material(m+1, current_score, current_calorie + calorie[m])

  
#   combine_material(0, 0, 0)
#   print(f'#{test_case} {result}')
  

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  N, L = map(int, input().split())
  s = []
  k = []
  def dfs(i, taste, kcal):
      global max_taste
      if kcal>L: # 칼로리 초과
          return
      if taste > max_taste: # 최대 칼로리 저장
          max_taste = taste
      if i==N: # 끝
          return
      dfs(i+1, taste + s[i], kcal + k[i]) # 현재 재료 선택
      dfs(i+1, taste, kcal) # 현재 재료 미선택
  for _ in range(N):
      score, kcal = map(int, input().split())
      s.append(score)
      k.append(kcal)
  max_taste = 0
  dfs(0,0,0)
  print(f'#{test_case} {max_taste}')