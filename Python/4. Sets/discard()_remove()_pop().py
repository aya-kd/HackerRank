n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    op = input().split()
    if op[0] == 'pop':
        s.pop()
    elif op[0] == 'remove':
        s.remove(int(op[1]))
    else:
        s.discard(int(op[1]))
       
print(sum(s))