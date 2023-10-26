from collections import namedtuple

N = int(input())
columns = input().split()
Student = namedtuple('Student',",".join(columns))
marks = []

for i in range(N):
    student_data = Student(*input().split())
    marks.append(int(student_data.MARKS))
    
print(sum(marks)/N)