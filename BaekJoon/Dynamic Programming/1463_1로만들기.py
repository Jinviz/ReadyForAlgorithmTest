N = int(input())
ctn = 0
arr = [0 for _ in range(N+1)]

for n in range(2,N+1):
    arr[n] = arr[n-1] + 1
    if n%2==0: arr[n] = min(arr[n//2] + 1, arr[n])
    if n%3==0: arr[n] = min(arr[n//3] + 1, arr[n]) 

print(arr[N])