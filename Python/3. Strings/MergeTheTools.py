def merge_the_tools(string, k):
    # your code goes here
    i = 0
    while(i<len(string)):
        print("".join(list(set(string[i:i+k]))))
        i += k