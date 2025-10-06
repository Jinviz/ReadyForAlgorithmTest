N = int(input())

for _ in range(N):
    T = int(input())
    arr = [0 for _ in range(12)]
    arr[1], arr[2], arr[3] = 1, 2, 4
    if T <= 3:
        print(arr[T])

    else:
        for n in range(4, T+1):
            arr[n] = arr[n-1] + arr[n-2] + arr[n-3]
        print(arr[T])