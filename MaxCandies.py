def kidswithcandies(candies, extracandies):
    res = []
    s = max(candies)
    for i in candies:
        res.append(i+extracandies>=s)
    return res
candies = [2,1,3]
extracandies = 1
print(kidswithcandies(candies,extracandies))