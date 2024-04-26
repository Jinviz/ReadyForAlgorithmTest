A, B = input().split()

def num_changer(num, action):
    arr = []
    for n in num:
        if action == "max":
            if n == '5':
                arr.append(6)
            else:
                arr.append(int(n))

        elif action == "min":
            if n == '6':
                arr.append(5)
            else:
                arr.append(int(n))
    changed_num = "".join(map(str, arr))
    return int(changed_num)

print(num_changer(A, "min") + num_changer(B, "min"), num_changer(A, "max") + num_changer(B, "max"))
