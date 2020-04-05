def maxProfit(prices) -> int:
    buy = 0
    sell = 0
    profit = 0
    for i in range(len(prices)):
        if prices[i] >= prices[sell]:
            sell = i
        else:
            if buy < sell:
                profit += prices[sell] - prices[buy]
            buy = sell = i
    if buy < sell:
        profit += prices[sell] - prices[buy]
    return profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([5,4,3,2,1]))

