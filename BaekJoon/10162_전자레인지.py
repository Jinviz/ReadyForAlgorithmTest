T = int(input())
button = [300,60,10]
count = [0,0,0]
for i, btn in enumerate(button):
    count[i], T = divmod(T, btn) 

if T:
    print(-1)
else:
    print(count[0],count[1],count[2])