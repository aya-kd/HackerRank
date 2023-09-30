import cmath

if __name__ == '__main__':
    #turn str input to comlex
    c = complex(input())
    r, theta = cmath.polar(c)
    print(r)
    print(theta)