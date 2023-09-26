def print_formatted(number):
    # your code goes here
    dec = ""
    oc = ""
    he = ""
    bi = ""
    
    #calculate the longest number -> ofc it's binary
    maxLen = 0
    for i in range(1, number+1):
        maxLen = len(bin(i)[2:])
        
    
    #Formatting the string using maxLen as alignement width
    for i in range(1, number+1):
        
        dec = " "*(maxLen-len(str(i))) + str(i) + " "
        oc = " "*(maxLen-len(oct(i)[2:])) + oct(i)[2:] + " "
        he = " "*(maxLen-len(hex(i)[2:])) + hex(i)[2:].title() + " "
        bi = " "*(maxLen-len(bin(i)[2:])) + bin(i)[2:]
        
        print(dec + oc + he + bi)