n,b = input().split()
n = reversed(n)
b = int(b)
n_case = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0

for i, letter in enumerate(n):
    sum += n_case.index(letter) * (b**i) 

print(sum)