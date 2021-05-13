def coinChange(coins, amount):
    memo = [0]
    for i in range(1, amount + 1):
        min = -1
        for coin in coins:
            if i - coin >= 0:
                if memo[i - coin] >= 0 and (min == -1 or memo[i - coin] + 1 < min):
                    min = memo[i - coin] + 1
        memo.append(min)
    return memo[amount]

print(coinChange([1, 2, 5], 11))
