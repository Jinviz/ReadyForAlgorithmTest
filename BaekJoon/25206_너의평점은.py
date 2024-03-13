data = [input().split() for _ in range(20)]
credit = []
grade = []
calc = 0.0
sum = 0.0
score = {
    'A+':   4.5,
    'A0':	4.0,
    'B+':	3.5,
    'B0':	3.0,
    'C+':	2.5,
    'C0':	2.0,
    'D+':	1.5,
    'D0':	1.0,
    'F':	0.0
}

for subject in data: 
    credit.append(float(subject[1]))
    grade.append(subject[2])

for i in range(len(credit)):
    if grade[i] != 'P':
        grade_score = score[grade[i]]
        calc += credit[i] * grade_score
    
for i, c in enumerate(credit):
    if grade[i] != 'P':
        sum += c

avg = round(calc / sum, 6)
print(avg)


# @깔끔한 풀이
# dic1 = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 
#         'D+':1.5, 'D0':1.0, 'F':0}
# c_t = 0
# g_t = 0
# for i in range(20):
#     s,c,g = input().split()
#     c = float(c)
#     g = str(g)
#     if g in dic1.keys():
#         c_t += c
#         g_t += dic1[g]*c
    
# print(g_t/c_t)