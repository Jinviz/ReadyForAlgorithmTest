import sys

T = int(sys.stdin.readline().strip()) 

for _ in range(T):
    M = int(sys.stdin.readline().strip())  
    yeon = set(map(int, sys.stdin.readline().strip().split()))  
    N = int(sys.stdin.readline().strip()) 
    dong = list(map(int, sys.stdin.readline().strip().split()))  

    for val in dong:
        print(1 if val in yeon else 0) 