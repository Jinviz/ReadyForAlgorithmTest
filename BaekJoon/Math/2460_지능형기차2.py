train = [tuple(map(int,input().split())) for _ in range(10)]
station_sum = [0 for _ in range(10)]
sum = 0

for n in range(10):
  sum += train[n][1] - train[n][0]
  station_sum[n] = sum

print(max(station_sum))