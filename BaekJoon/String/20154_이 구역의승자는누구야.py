LETTER_SCORES = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 3,
    'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 3,
    'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1,
    'V': 1, 'W': 2, 'X': 2, 'Y': 2, 'Z': 1
}

S = input()
# scores = []
sum = 0 
for s in S:
  # scores.append(LETTER_SCORES[s])
  sum += LETTER_SCORES[s]

# while len(scores) > 1:
#   for n in range(len(scores)):
#     if n + 1 < len(scores):
#       scores[n] = (scores[n] + scores[n+1]) % 10
#       scores.pop(n+1)

if sum%2:
  print("I'm a winner!")
else:
  print("You're the winner?")


# 기존 논리 흐름 풀이는 시간 초과
# 그냥 다 더하고 나누면 된다..