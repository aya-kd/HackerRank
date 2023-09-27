n = int(input())
eng = set(map(int, input().split()))
m = int(input())
fr = set(map(int, input().split()))

#total number of students who have subscribed to at least one newspaper.
print(len(eng.union(fr)))


#or
print(len(eng | fr))