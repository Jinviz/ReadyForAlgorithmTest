N, M = map(int, input().split())
number = [str(n) for n in range(1,N+1)]

def progression(case, num):
    if len(case) == M:
        result = " ".join(case)
        print(result)
        return
    
    for n in num:
        case.append(n)
        num_list = num[:]
        num_list.remove(n)
        progression(case, num_list)
        case.pop()

progression([], number)