octal = input()

binary = bin(int(octal, 8))[2:]

print(binary)


# 포맷함수 구현
# octal = input()
# binary = ''

# for digit in octal:
#     binary += format(int(digit), '03b')

# print(int(binary))


# 직접 구현
# from collections import deque
# n = int(input())
# decimal = deque([])
# binary = deque([])

# while True:
#     if n < 8: 
#         decimal.appendleft(str(n))
#         break
#     decimal.appendleft(str(n%8))
#     n = n//8

# n = int(''.join(decimal))
# print(n)

# while True:
#     if n < 2: 
#         binary.appendleft('1')
#         break
#     binary.appendleft(str(n%2))
#     n = n//2
    
# print(''.join(binary))
        