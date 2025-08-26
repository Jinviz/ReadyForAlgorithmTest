from collections import deque

while True:
    case = list(map(int,input().split()))
    if case[0] == 0:
        break
    s = case[1:]

    def lotto_machine(start=0, lotto=[]):
        if len(lotto) == 6:
            print(' '.join(map(str, lotto)))
            return
        
        for i in range(start, len(s)):
            lotto.append(s[i])
            lotto_machine(i + 1, lotto)
            lotto.pop()

    lotto_machine()
