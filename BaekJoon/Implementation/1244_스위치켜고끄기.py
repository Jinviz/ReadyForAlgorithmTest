# 남학생(1): 자기가 받은 수의 배수 번호를 갖는 스위치의 상태를 바꾸기 
# 여학생(2): 자기가 받은 수를 기준으로 가장 넓은 범위의 대칭 범위를 찾아 모두 바꾸기

n_lights = int(input())
state = list(map(int, input().split()))
n_students = int(input())

for _ in range(n_students):
    gender, number = map(int, input().split())
    # 남학생이면
    if gender == 1:
        switch_num = [number*(n+1) for n in range(len(state)//number)]
        for switch in switch_num:
            state[switch-1] = 0 if state[switch-1] == 1 else 1
    
    # 여학생이면
    else:   
        for n in range(number):
            if number+n > len(state):
                break
            num = number-1 # 리스트 번호 고려
            if state[num-n] == state[num+n]:
                state[num-n] = 0 if state[num-n] == 1 else 1
                if(n != 0):
                    state[num+n] = 0 if state[num+n] == 1 else 1
            else:
                break
    
output_line = len(state) // 20
if output_line == 0:
    print(' '.join(map(str, state))) 
else:
    for n in range(output_line):
        print(' '.join(map(str, state[n*20:n*20+20])))
    if len(state) % 20 != 0:
        print(' '.join(map(str, state[output_line*20:])))


# REVIEW
# 리스트의 번호가 -1이란 것이 헷갈리게 하는 포인트이다. 적절히 인덱스 번호를 자유자재로 컨트롤 할 수 있어야 하는 문제.