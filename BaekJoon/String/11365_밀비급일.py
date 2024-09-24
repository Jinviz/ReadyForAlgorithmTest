import sys

lines = []
while True:
    line = sys.stdin.readline().rstrip()
    if line == 'END':
        break
    lines.append(line[::-1])

for s in lines:
    print(s)