T = int(input())

for _ in range(T):
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    
    #chech if the intersection between a and b == a
    print(a & b == a)