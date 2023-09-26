if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

 #marks average of a given student   
    score = student_marks[query_name]
    y=0
    for x in score:
        y = y+x
    av = y/len(score)
    print("%.2f" %av)