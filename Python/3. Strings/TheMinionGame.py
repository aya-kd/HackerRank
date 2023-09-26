def minion_game(string):
    # your code goes here
    vow = "AEUIO"
    k = 0
    s = 0
    
    #finding all substrings
    for i in range(len(string)):
        if string[i] in vow:
            k += len(string)-i
        else:
            s += len(string)-i
    
    if s > k:
        print(f"Stuart {s}")
    elif s < k:
        print(f"Kevin {k}")
    else:
        print("Draw")
