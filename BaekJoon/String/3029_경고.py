h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
t = t2 - t1 if t2 > t1 else t2-t1+24*60*60
h = t//60//60
m = t//60 % 60
s = t%60
print("%02d:%02d:%02d" % (h, m, s))

# current_time = list(map(int, input().split(':')))
# bomb_time = list(map(int, input().split(':')))

# hour, minute, second = 0,0,0

# if current_time[2] > bomb_time[2]:
#     second += 60 - current_time[2] + bomb_time[2]
#     minute -= 1  # 분을 하나 빼야 함
# else:
#     second += bomb_time[2] - current_time[2]

# if current_time[1] > bomb_time[1]:
#     minute += 60 - current_time[1] + bomb_time[1]
#     hour -= 1  # 시간을 하나 빼야 함
# else:
#     minute += bomb_time[1] - current_time[1]

# if current_time[0] > bomb_time[0]:
#     hour += 24 - current_time[0] + bomb_time[0]
# else:
#     hour += bomb_time[0] - current_time[0]

# result = [hour, minute, second]
# result = [str(r).rjust(2, '0') for r in result]
# print(":".join(result))

# 마이너스가 될 때 조건도 고려해줘야 하는 거 같음