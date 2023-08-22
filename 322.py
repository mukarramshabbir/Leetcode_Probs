def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for i in range(1,amount+1):
        for coin in coins:
            if i>=coin:
                dp[i]=min(dp[i],dp[i-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1
    

if __name__=="__main__":
    coins = [1,2,5]
    amount = 11
    result = coinChange(coins,amount)
    print(result)