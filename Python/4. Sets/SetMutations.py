a = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    mut = input().split()
    s = set(map(int, input().split()))
    
    if mut[0] == 'intersection_update':
        A &= s
    elif mut[0] == 'update':
        A.update(s)
    elif mut[0] == 'symmetric_difference_update':
        A ^= s
    else:
        A -= s

print(sum(A))