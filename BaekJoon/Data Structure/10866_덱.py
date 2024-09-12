from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
deck = deque([])

for _ in range(N):
    command = input().split()
    do_it = command[0]
    
    if do_it == 'push_front':
        deck.appendleft(command[1])
    elif do_it == 'push_back':
        deck.append(command[1])
    elif do_it == 'pop_front':
        print(deck.popleft() if deck else -1)
    elif do_it == 'pop_back':
        print(deck.pop() if deck else -1)
    elif do_it =='size':
        print(len(deck))
    elif do_it == 'empty':
        print(1 if len(deck) == 0 else 0)
    elif do_it == 'front':
        print(deck[0] if deck else -1)
    else:
        print(deck[-1] if deck else -1)
    
    
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
