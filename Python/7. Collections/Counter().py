from collections import Counter

X = int(input())
shoes = list(map(int, input().split()))
N = int(input())
prices = []

#count the number of availables shoes of each size
counter = Counter(shoes)
sizes = list(Counter(shoes).keys())


for i in range(N):
    #read the client's order
    size, x = list(map(int, input().split()))
    
    #if the size exists
    if size in sizes and counter[size] > 0:
        #add the price to prices
        prices.append(x)
        #remove 1 of the availables shoes
        counter[size] -= 1

#sum all the prices
print(sum(prices))