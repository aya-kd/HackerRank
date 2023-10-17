from itertools import product
if __name__ == '__main__':
    K, M = map(int, input().split())
    l = []
    S = []
    
    for i in range(K):
        inp = list(map(int, input().split()))
        l.append(inp[1:])
    
    #calculate all possible combinations
    comb_list = list(product(*l))

    #calculate S for each element in comb_list
    for i in comb_list:
         S.append(sum(x**2 for x in i)%M)
    
    #print the result
    print(max(S))