import sys

N, M = map(int, input().split())

S = set()
count = 0

for n in range(N):
    S.add(sys.stdin.readline().rstrip())

for m in range(M):
    inspect = sys.stdin.readline().rstrip()
    if inspect in S:
        count += 1
    
print(count)

# 빠른 검색을 이용하기 위해 리스트(list)말고 집합(set)을 이용하였다.
# set의 요소 추가는 append가 아닌 add로 추가할 수 있다.
# 요소가 있는지 확인하는 가장 빠른 방법은 집합을 이용하여 검사할 수 있다.
# 요소가 존재하는데 몇 번째 데이터인지 확인하려면 dict로 바로 검색하는 방법을 이용하면 된다. e.g. 1620번문제