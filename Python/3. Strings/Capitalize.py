def solve(s):
    s = s.title()
    res = ""
    
    for i in range(len(s)):
        if s[i-1] == '0' or s[i-1] == '1' or s[i-1] == '2' or s[i-1] == '3' or s[i-1] == '4':
            res += s[i].lower()
            i += 2
        else:
            res += s[i]  

    return res