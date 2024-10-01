# 시간당 피로도 축적 A
# 시간당 처리 일량 B
# 시간당 피로도 감소 C 
# 최대 피로도 M

A, B, C, M = map(int, input().split())
stamina,count,work = 0, 0, 0



for _ in range(24):
    if M < stamina + A:
        stamina -= C
    else:
        stamina += A
        work += B

    if stamina < 0:
        stamina = 0

print(work)
# while True:
#     if A > M:
#         break
#     count += 1
#     stamina += A
#     remained_time = 24 - count
#     enable_stamina = (stamina - M) - (remained_time * C)
#     if enable_stamina <= 0:
#         continue
#     else:
#         count -= 1
#         break

# print(B*count)
