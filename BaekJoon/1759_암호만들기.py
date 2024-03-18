L, C = input.split()
alpha = list(input.split())
vowel = ['a', 'e', 'i', 'o', 'u']
total = []
case = []
cnt = 0
# 최소 한개 모음, 최소 두개 자음, 오름차순

# 조합(재귀)
def Combination(alpha):
    case.append(alpha[0])
    alpha.remove(a)
    cnt += 1