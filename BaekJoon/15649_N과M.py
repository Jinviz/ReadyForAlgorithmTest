N, M = map(int, input().split())
number = [str(n) for n in range(1,N+1)]
print(number)
case = list()

def progression(first, num):
    if len(case) == M:
        result = " ".join(case)
        print(result)
        case.pop()
    
    else:
        for n in num:
            case.append(n)
            print(case)
            num.remove(n)
            progression(False, num)

progression(True, number)

    
        
    