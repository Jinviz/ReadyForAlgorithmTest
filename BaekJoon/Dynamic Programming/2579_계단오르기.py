N = int(input())
stairs = [[int(input()),0,0] for _ in range(N)]
stairs[0][1], stairs[0][2] = stairs[0][0], stairs[0][0]  

if N > 1:
    stairs[1][1], stairs[1][2] = stairs[1][0], stairs[1][0]+stairs[0][0] 

for n in range(2, N):
    stairs[n][1] = max(stairs[n-2][1]+stairs[n][0], stairs[n-2][2]+stairs[n][0])
    stairs[n][2] = stairs[n-1][1]+stairs[n][0]

print(max(stairs[N-1][1:3]))