def recursion(s, l, r, count):
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

T = int(input())
test_case = [input() for _ in range(T)]

for case in test_case:
    isPalin, count = isPalindrome(case)
    print(isPalin, count)