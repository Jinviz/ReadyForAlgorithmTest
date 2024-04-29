N = int(input())
letter = [input() for _ in range(N)] 

letter = sorted(set(letter), key = lambda x: (len(x), x))

for l in letter:
    print(l)