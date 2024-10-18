N = int(input())
find_num = input()

snail = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = (N-1)//2, (N-1)//2
snail[x][y] = 1
count = 1

while not(x==0 and y==0):
    for i in range(4):
        if (x,y) == (0,0): break
        while True:
            count += 1
            snail[x+dx[i]][y+dy[i]] = count
            x, y = x+dx[i], y+dy[i]
            if (x,y) == (0,0): break
            elif (i+1 < 4):
                if snail[x+dx[i+1]][y+dy[i+1]] == 0:
                    break
            else:
                if snail[x+dx[0]][y+dy[0]] == 0:
                    break
                    
for i in snail:
    print(' '.join(map(str, i)))

for a in range(len(snail)):
    if int(find_num) in snail[a]:
        snail[a] = list(map(str, snail[a]))
        b = snail[a].index(find_num)
        print(a+1, b+1)