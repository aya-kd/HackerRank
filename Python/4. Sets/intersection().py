n = int(input())
eng = set(map(int, input().split()))
m = int(input())
fr = set(map(int, input().split()))

#total number of students who have subscribed to both newspapers.
print(len(eng.intersection(fr)))


#or
print(len(eng & fr))