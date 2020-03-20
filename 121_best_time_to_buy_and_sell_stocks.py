def maxProfit(prices):
    times = [0, 0, 0]
    for i in range(1, len(prices)):
        if prices[i] - prices[times[2]] > prices[times[1]] - prices[times[0]]:
            times = [times[2], i, times[2]]
        if prices[i] < prices[times[2]]:
            times[2] = i
    return prices[times[1]] - prices[times[0]]

print(maxProfit([7,1,5,3,6,4]))