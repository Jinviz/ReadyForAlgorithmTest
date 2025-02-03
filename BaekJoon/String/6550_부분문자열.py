import sys

while True:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    S,T = line.split()

    correct_goal = len(S)
    count = 0

    for s in S:
      for index, t in enumerate(T):
        T = T[1:]
        if s == t:
          count += 1
          break
    
    if correct_goal == count:
      print("Yes")
    else:
      print("No")