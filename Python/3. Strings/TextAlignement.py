N = int(input())

for i in range(0,N):
    #print(pat)
    print(("H"*(i*2+1)).center(N*2-1))
 
for _ in range(0, N+1):
    print(("H"*N).center(N*2-1) + " "*(N*2+1) + ("H"*N).center(N*2-1))
    
for _ in range(0, N//2+1):
    print(("H"*N*5).center(N*5+2*((N*2-1-N)//2)))

for _ in range(0, N+1):
    print(("H"*N).center(N*2-1) + " "*(N*2+1) + ("H"*N).center(N*2-1))

for i in range(N,0,-1):
    #print(pat)
    print((" "*N).center(N*2-1) + " "*(N*2+1) + ("H"*(i*2-1)).center(N*2-1))