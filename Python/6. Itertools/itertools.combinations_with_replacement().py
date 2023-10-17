from itertools import combinations_with_replacement

if __name__ == '__main__':
    s,k = input().split()
    s = sorted(s)
    k = int(k)
    
    #get all combinations list
    comb_list = list(combinations_with_replacement(s,k))
    
    #printing combinations
    for i in comb_list:
        print("".join(i))