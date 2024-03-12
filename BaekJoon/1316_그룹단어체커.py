num = int(input())
data = [input() for _ in range(num)]
group_num = 0

for word in data:
    check = []
    group_check = True
    for i in range(len(word)):  
        check.append(word[i])
        if(i != len(word)-1):
            if word[i] != word[i+1]:
                if  word[i+1] in check:
                    group_check = False
                    break
    if group_check:
        group_num += 1

print(group_num)