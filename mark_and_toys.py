def maximumToys(prices, k):
    prices.sort()
    sum,toys = 0
    for i in prices:
        if (sum + i) <= k:
            sum += i
            toys += 1
        else:
            break
    return toys

