if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
    l1 = [x for x in range(x+1)]
    l2 = [y for y in range(y+1)]
    l3 = [z for z in range(z+1)]
    
    
    l4 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(l4)