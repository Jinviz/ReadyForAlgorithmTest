from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        rank = [tuple(map(int, input().split())) for _ in range(N)]
        rank.sort(key=lambda x : x[0])
        top = rank[0][1] 
        count = 1
        
        for r in range(1,N):
            if rank[r][1] < top :
                count += 1
                top = rank[r][1]
                
        print(count)   

# 시간 초과
# from sys import stdin
# input = stdin.readline

# if __name__ == "__main__":
#     case = int(input())
#     volunteers = []
#     for a in range(case):
#         n = int(input())
#         volunteers = sorted([tuple(map(int, input().split())) for _ in range(n)])
#         count = n
#         for m, volunteer in enumerate(volunteers):
#             interview = [volun[1] for volun in volunteers[0:m]] 
#             if interview and volunteer[1] > min(interview):
#                 count -= 1
#         print(count)
