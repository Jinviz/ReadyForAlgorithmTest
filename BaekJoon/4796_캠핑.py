from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    L = []
    P = []
    V = []
    case = 0

    while True:
        l, p, v = map(int, input().split())
        if l == p == v == 0:
            break
        else: 
            L.append(l)
            P.append(p)
            V.append(v)
            case += 1

    for i in range(case):
        quotient, remainder = divmod(V[i], P[i])
        result = L[i] * quotient + remainder
        print('Case %d: %d'%(i+1, result))
