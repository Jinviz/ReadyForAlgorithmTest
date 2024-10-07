from collections import deque

queue = deque([i for i in input()])
arrow_state = False
stack = []
reversed_S = ""

for _ in range(len(queue)):
    q = queue.popleft()
    if not arrow_state:
        if q == '<':
            if len(stack) > 0:
                reversed_S += ''.join(list(reversed(stack)))
                stack = []
            reversed_S += q
            arrow_state = True
        elif q == ' ':
            reversed_S += ''.join(list(reversed(stack))) + q 
            stack = []
        else:
            stack.append(q)

    else:
        reversed_S += q
        if q == '>':
          arrow_state = False
if len(stack) > 0:
    reversed_S += ''.join(list(reversed(stack)))

print(reversed_S)


### 밑의 풀이는 정규표현식 풀이이다.
# import re

# r = re.compile('<[a-z ]+>|[a-z0-9 ]+')
# regs = r.findall(input())


# ans = ''
# for x in regs:
#     if x[0] == '<':
#         ans += x
#     else:
#         temp = x.split(' ')
#         rev = []
#         for y in temp:
#             y = y[::-1]
#             rev.append(y)
#         rev = " ".join(rev)
#         ans += rev

# print(ans)