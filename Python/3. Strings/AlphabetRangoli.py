def print_rangoli(size):
    s = ""
    l = []
    # your code goes here
    alph = "abcdefghijklmnopqrstuvwxyz"
    
    #The upper part
    for i in range(size-1,-1,-1):
        if len(s) == 0:
            s += alph[i]
            l = list(s)
            print(s.center(size*2-1 + size*2-2, "-"))           
            
        else:
            s += alph[i]
            l = list(s + s[:len(s)-1][::-1])
            print(("-".join(l)).center(size*2-1 + size*2-2, "-"))
            
    #The lower part
    for i in range(len(s)-1, 0, -1):
        
            s = s[:i]
            l = list(s + s[:len(s)-1][::-1])
            print(("-".join(l)).center(size*2-1 + size*2-2, "-"))