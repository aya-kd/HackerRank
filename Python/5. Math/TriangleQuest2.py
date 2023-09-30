#only one for is allowed :(
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(10**(i-1) * sum([j*pow(10,i-j) for j in range(i,0,-1)]) + sum([j*pow(10,j-1) for j in range(i-1,0,-1)]))