def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n<=2:
        return n
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
    
if __name__=="__main__":
    k = 5
    res=climbStairs(k)
    print(res)