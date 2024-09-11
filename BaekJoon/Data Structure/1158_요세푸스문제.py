N,K = map(int, input().split())

next = K-1
sequence = str()
people = [i for i in range(1,N+1)]

for i in range(N):
    if i == N-1:
        sequence += str(people[next])
    else:
        sequence += f"{people[next]}, "
    people.pop(next)
    if len(people):
        next = (next+K-1) % len(people) 

print(f"<{sequence}>")