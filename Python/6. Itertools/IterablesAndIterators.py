from itertools import combinations
if __name__ == '__main__':
    N = int(input())
    l = list(input().split())
    K = int(input())
    
    #list of all combinations
    comb_list = list(combinations(l, K))
    
    #calculating number of tuples that conatain 'a'
    count = 0
    for i in comb_list:
        if 'a' in i:
            count += 1
            
    #calculation the probability
    print(count/len(comb_list))