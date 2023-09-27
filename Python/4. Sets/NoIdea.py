if __name__ == '__main__':
    n,m = map(int,input().split()) 

    #read array elements:
    arr = list(map(int,input().split()))

    #read A
    A = set(map(int,input().split()))

    #read B
    B = set(map(int,input().split()))
    
    #calculate happiness:
    happ = 0
    for i in arr:
        if i in A:
            happ += 1
        if i in B:
            happ -= 1
    print(happ)