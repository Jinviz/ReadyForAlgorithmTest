T = int(input())
case = [int(input()) for _ in range(T)]
cent = [25, 10, 5, 1]

cent_num = [[0,0,0,0] for _ in range(T)]

for i, t in enumerate(case):
    for n in range(4):
        num, t = divmod(t, cent[n])
        cent_num[i][n] = num 

for n in cent_num:
    print(n[0],n[1],n[2],n[3])