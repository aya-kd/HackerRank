import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    #MBC = MCB
    tanMCB = AB/BC
    MCB = math.degrees(math.atan(tanMCB))
    print(f"{round(MCB)}{chr(176)}")