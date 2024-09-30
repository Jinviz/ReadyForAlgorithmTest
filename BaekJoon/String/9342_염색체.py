import sys
import re

N = int(input())
case = [sys.stdin.readline().rstrip() for _ in range(N)]

expression = re.compile('^[A-F]?A+F+C+[A-F]?$')

for per in case:
    if expression.match(per):
        print('Infected!')
    else:
        print('Good')