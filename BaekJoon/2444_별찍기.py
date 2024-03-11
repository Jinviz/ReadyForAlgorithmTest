case = int(input())
dump = list()
star = list()
for n in range(case):
    for i in range(case-1-n):
        dump.append(' ')
    for i in range(2*n + 1):
        dump.append('*')
    star.append("".join(dump))
    print(star[n])
    dump.clear()

for s in reversed(star):
    if(s != star[-1]):   
        print(s)