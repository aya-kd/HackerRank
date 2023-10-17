from itertools import combinations

if __name__ == '__main__':
    S, k = input().split()
    S = sorted(S)
    k = int(k)
    comb_list = []
    
    #get all combinations list
    for i in range(1,k+1):
        comb_list.extend(combinations(S, i))
        
    #print combination
    for i in comb_list:
        print("".join(i))