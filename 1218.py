def longestSubsequence(arr, difference):
    """
    :type arr: List[int]
    :type difference: int
    :rtype: int
    """
    dp={}
    for num in arr:
        prev_num=num-difference
        dp[num]=dp.get(prev_num,0)+1
    return max(dp.values())

if __name__=="__main__":
    arr = [1,5,7,8,5,3,4,2,1]
    difference = -2
    res=longestSubsequence(arr,difference)
    print(res)