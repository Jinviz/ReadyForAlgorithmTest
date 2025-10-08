import copy

def solution(friends, gifts):
    numbering = {friend: idx for idx, friend in enumerate(friends)}
    
    N = len(friends) 
    gift_point = {n: 0 for n in range(N)}
    gift_count = copy.copy(gift_point)
    gift_table = [[0 for _ in range(N)] for _ in range(N)]
    for gift in gifts:
        a, b = gift.split()
        gift_point[numbering[a]] += 1
        gift_point[numbering[b]] -= 1
        
        r, c = numbering[a], numbering[b]
        gift_table[r][c] += 1
    
    for n in range(N):
        for m in range(n+1, N):
            A, B = gift_table[n][m], gift_table[m][n]
            if A > B:
                gift_count[n] += 1
            if A < B:
                gift_count[m] += 1
            if A == B:
                if gift_point[n] > gift_point[m]:
                    gift_count[n] += 1
                if gift_point[n] < gift_point[m]:
                    gift_count[m] += 1
    
    values = gift_count.values()
    return max(values)
    