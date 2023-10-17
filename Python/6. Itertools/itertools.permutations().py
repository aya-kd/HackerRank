from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()
    k = int(k)
    
    for i in sorted(list(permutations(S, k))):
        print("".join(i))