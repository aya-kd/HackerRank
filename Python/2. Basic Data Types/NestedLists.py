if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    
    scores = [x[1] for x in records]
    second_lowest_score = sorted(tuple(set(scores)))[1]
    
    names = sorted([x[0] for x in records if x[1] == second_lowest_score])
    for x in names:
        print(x)