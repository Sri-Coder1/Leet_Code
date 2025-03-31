def canplaceflower(flowerbed,n):
    c=0
    i=0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0 ):
            flowerbed[i] = 1
            c=c+1
        i = i+1
    return c>=n
flowerbed = [1,0,0,0,1,0,0]
n = int(input("enter the number of flowers to be placed"))
print(canplaceflower(flowerbed,n))