data = [int(input()) for _ in range(9)]
print(data)

for a in range(len(data)-6):
    for b in range(1, len(data)-5):
        for c in range(2, len(data)-4):
            for d in range(3, len(data)-3):
                for e in range(4, len(data)-2):
                    for f in range(5, len(data)-1):
                        for g in range(6, len(data)):
                            dump = [data[a], data[b], data[c], data[d], data[e], data[f], data[g]]
                            if len(set(dump)) == len(dump) and sum(dump) == 100:
                                case = sorted(dump)
                            dump.clear()

for i in case:
    print(i)