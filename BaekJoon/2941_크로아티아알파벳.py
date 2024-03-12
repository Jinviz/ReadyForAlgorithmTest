data = input()
count = 0

for index, d in enumerate(data):
    pre_index = index - 1
    if d == '=':
        if data[pre_index] == 'c':
            count += 1
        elif data[pre_index] == 'z':
            count += 1
        elif data[pre_index] == 's':
            count += 1
    elif d == '-':
        if data[pre_index] == 'c' or data[pre_index] == 'd':
            count += 1
    elif d == 'j':
        if data[pre_index] == 'l' or data[pre_index] == 'n':
            count += 1 

print(count)