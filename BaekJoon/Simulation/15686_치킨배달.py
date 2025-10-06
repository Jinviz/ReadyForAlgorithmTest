import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
all_chicken, all_house = [], []
result = []

for n in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for m in range(N): 
        if row[m] == 1:
            all_house.append((n, m))
        elif row[m] == 2:
            all_chicken.append((n, m))

def calculate_chicken_length(chicken_list):
    city_chicken_length = 0
    for house in all_house:
        chicken_length = []
        for chicken in chicken_list:
            chicken_length.append(abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))    
        city_chicken_length += min(chicken_length)
        
    return city_chicken_length

def dfs(start=0, chicken_list=[]):
    if len(chicken_list) == M:
        result.append(calculate_chicken_length(chicken_list))
        return

    for idx in range(start, len(all_chicken)):
        new_chicken_list = chicken_list[:]
        new_chicken_list.append(all_chicken[idx]) 
        dfs(idx+1, new_chicken_list)


dfs()
print(min(result))