import math
data = input()
count = 0
for n in range(1, len(data)):
    if data[n] != data[n-1]:
        count +=1
if count < 2:
    print(count)
else:
    print(math.ceil(count/2))