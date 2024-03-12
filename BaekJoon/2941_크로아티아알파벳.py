data = input()
count = 0

for index, d in enumerate(data):
    pre_index = index - 1
    if d == '=':
        if data[pre_index] == 'c':
            continue
        elif data[pre_index] == 'z':
            if data[pre_index -1] == 'd':
                count -= 1
            else:
                continue
        elif data[pre_index] == 's':
            continue
    elif d == '-':
        if data[pre_index] == 'c' or data[pre_index] == 'd':
            continue
    elif d == 'j':
        if data[pre_index] == 'l' or data[pre_index] == 'n':
            continue
        else:
            count += 1
    else:
        count += 1
print(count)