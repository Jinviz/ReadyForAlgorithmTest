N = int(input())
main = int(input())
ticket = [int(input()) for _ in range(N-1)]
result = 0

if N==1:
    print(0)
    exit(0)

while max(ticket) >= main:
    idx = ticket.index(max(ticket))
    ticket[idx] -= 1
    main += 1
    result += 1

print(result)
