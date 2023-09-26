if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    runner_up = sorted(tuple(set(arr)))[-2]
    print(runner_up)
    
#array -> set: elemenate duplicates
#set -> tuple: to sort it