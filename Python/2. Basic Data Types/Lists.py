N = int(input())
l = []
for x in range(0,N):
    inp = input().split()
    #print(inp)
    op = str(inp[0])
    #print(op)
        
        
    if op == 'insert':
        l.insert(int(inp[1]), int(inp[2]))
    if op == 'print':
        print(l)
    if op == 'remove':
        l.remove(int(inp[1]))
    if op == 'append':
        l.append(int(inp[1]))
    if op == 'sort':
        l.sort()
    if op == 'pop':
        l.pop()
    if op == 'reverse':
        l.reverse()