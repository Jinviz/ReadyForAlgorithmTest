import sys
N = int(input())
files = {}

for _ in range(N):
    file = sys.stdin.readline().rstrip()
    dot = file.find('.')
    if file[dot+1:] in files:
        files[file[dot+1:]] += 1
    else:
        files[file[dot+1:]] = 1

file_count = sorted(files.items())
for f in file_count:
    print(' '.join(map(str,f)))