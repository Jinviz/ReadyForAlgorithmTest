formula = input().split('-')
result = 0

for i,terms in enumerate(formula):
    if '+' in terms:
        sum = 0 
        letter = terms.split('+')
        for l in letter:
            sum += int(l)
        result -= sum
    else:
        result -= int(terms)
    
    # 첫번째 항은 부호 변경
    if i == 0:
        result = -result

print(result)