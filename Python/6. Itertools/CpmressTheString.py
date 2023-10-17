from itertools import groupby

if __name__ == '__main__':
    s = input()
    key_func = lambda x: int(x) #treatement of each element of the iterable
    l = []
    
    for key, group in groupby(s, key_func):
        l.append((len(list(group)),key)) 
        #key is the single occurence of each item
        
    print(" ".join(map(str,l)))