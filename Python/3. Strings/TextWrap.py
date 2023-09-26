def wrap(string, max_width):
    res = ""
    for i in range(len(string)):
        if i%max_width == 0:
            res += string[i:i+max_width] + "\n"
    return res