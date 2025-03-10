from collections import Counter

N = int(input())
participant = Counter(input() for _ in range(N))
clear = Counter(input() for _ in range(N - 1))

for name in participant:
    if participant[name] != clear[name]: 
        print(name)
        break