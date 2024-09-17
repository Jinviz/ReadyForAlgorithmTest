import sys

N, M = map(int, input().split())
collections_number = {}
collections_name = {}

for n in range(1, N+1):
    pocketmon = sys.stdin.readline().rstrip()
    collections_number[n] = pocketmon
    collections_name[pocketmon] = n
    
for _ in range(M):
    query = sys.stdin.readline().rstrip()
    if query.isdigit():
        print(collections_number[int(query)])
    else:
        print(collections_name[query])
