N, M = map(int, input().split())
number = [str(n) for n in range(1,N+1)]
case = list()

def progression(first, excep):
    if len(case) == M:
        result = ' '.join(case)
        print(result)
        return
    
    else:
        if first == True:
            for n in number:
                case.append(n)
                progression(False, n)

        else:
            for n in number:
                if n != excep:
                    case.append(n)
                    progression(False, excep)

progression(True, '')

    
        
    