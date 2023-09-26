inp = input()
inp = inp.split() 
N = int(inp[0])
M = N*3
pat = ".|."
res = ""

for i in range(0,N//2):
    #print(pat)
    print((pat*(i*2+1)).center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(N//2,0,-1):
    #print(pat)
    print((pat*(i*2-1)).center(M, "-"))