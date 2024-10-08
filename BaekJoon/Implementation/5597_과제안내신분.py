students = [n for n in range(1,31)]

for _ in range(28):
    submit = int(input())
    students.remove(submit)


print(students[0])
print(students[1])