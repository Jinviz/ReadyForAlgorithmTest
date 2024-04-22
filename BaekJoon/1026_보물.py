length = int(input())
A = list(reversed(sorted(list(map(int, input().split())))))
B = sorted(list(map(int, input().split())))

# 가장 큰 수와 가장 작은 수를 곱해야 함
sum = 0
for i in range(length):
    sum += A[i] * B[i]

print(sum)