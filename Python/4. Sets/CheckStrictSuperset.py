A = set(map(int, input().split()))
n = int(input())
isSuperset = True


for _ in range(n):
    s = set(map(int, input().split()))
    if s & A != s:
        isSuperset = False
        break

print(isSuperset)