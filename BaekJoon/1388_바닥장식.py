n,m = map(int, input().split())
design = [list(input()) for _ in range(n)]

# '-'모양의 나무 판자 개수 계산
count = 0
for i in range(n):
    a = ''
    for j in range(m):
        if design[i][j] == '-':
            if design[i][j] != a:
                count += 1
        a = design[i][j]
 
# 'ㅣ'모양의 나무 판자 개수 계산
for j in range(m):
    a = ''
    for i in range(n):
        if design[i][j] == '|':
            if design[i][j] != a:
                count += 1
        a = design[i][j]
 
print(count)