data = input().upper()
alpa = list(set(data))
alpa_cnt = []

for a in alpa:
    dump = data.count(a)
    alpa_cnt.append(dump)

if alpa_cnt.count(max(alpa_cnt)) > 1:
    print('?')
else:
    alpa_max = alpa_cnt.index(max(alpa_cnt))
    print(alpa[alpa_max])


