data = input()
dump = list()

for d in data:
    dump.append(d)
reverse = ''.join(reversed(dump))

if(data == reverse):
    print(1)
else:
    print(0)
