M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

#calculate the difference and sorting it
diff = sorted(list(a.symmetric_difference(b)))

for i in diff:
    print(i)