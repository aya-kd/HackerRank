# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(map(int, input().split()))
m = int(input())
fr = set(map(int, input().split()))

# total number of students who have subscribed to either the English or the French newspaper but not both.
print(len(eng.symmetric_difference(fr)))


# or
print(len(eng ^ fr))