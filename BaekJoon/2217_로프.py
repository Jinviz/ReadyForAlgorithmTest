N = int(input())
rope = sorted([int(input()) for _ in range(N)])

result = [] 
#  모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
for n in range(N):
    result.append(rope[n] * (N-n))

max_weight = max(result)
print(max_weight)