def count_substring(string, sub_string):
    
    count = 0
    for i in range(len(string)):
        s = string[i:i+len(sub_string)]
        if s == sub_string:
            count += 1
    
    return count