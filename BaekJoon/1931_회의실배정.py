N = int(input())
# 1st.끝나는 시간이 빠른 순대로 오름차순 정렬
# 2nd.시작시간이 빠른 순대로 오름차순 정렬 # 이유: 22 12일 경우 회의를 두번 할 수 있음에도 22 다음 12가 올 수 없어서 1번 회의한 걸로 간주됨 
time = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x: (x[1], x[0]))

conference = pre_end = 0

for section in time:
    if section[0] >= pre_end:
        conference += 1
        pre_end = section[1]

print(conference)
