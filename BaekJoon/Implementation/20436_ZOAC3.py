# 쿼터식 키보드 알파벳 위치
keyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ''], 
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']     
]

key_map = {
    'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
    'a': 0, 's': 0, 'd': 0, 'f': 0, 'g': 0, 'h': 1, 'j': 1, 'k': 1, 'l': 1,
    'z': 0, 'x': 0, 'c': 0, 'v': 0, 'b': 1, 'n': 1, 'm': 1
} 

l, r = input().split()
alpha = input()
consonant, vowels = [], [] 
time = 0

for a in alpha:
    if key_map[a] == 0:
        consonant.append(a) 
    else:
        vowels.append(a)

def find_position(char):
    for i, row in enumerate(keyboard):
        if char in row:
            return i, row.index(char)
    return None

for n in range(1, len(consonant)):
    x1, y1 = find_position(consonant[n-1])
    x2, y2 = find_position(consonant[n])
    distance = abs(x2 - x1) + abs(y2 - y1)
    time += distance

for n in range(1, len(vowels)):
    x1, y1 = find_position(vowels[n-1])
    x2, y2 = find_position(vowels[n])
    distance = abs(x2 - x1) + abs(y2 - y1)
    time += distance

time += len(alpha)
print(time)
