s = input()
    
alphanum = False
alpha = False
digit = False
low = False
up = False
    
for x in s:
    if x.isalnum():
        alphanum = True
    if x.isalpha():
        alpha = True
    if x.isdigit():
        digit = True
    if x.islower():
        low = True
    if x.isupper():
        up = True    

print(alphanum)
print(alpha)
print(digit)
print(low)
print(up)