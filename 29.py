def getAverages(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    n=len(nums)
    avgs=[0]*n
    cum_sum=[0]*(n+1)
    for i in range(1,n+1):
        cum_sum[i]=cum_sum[i-1]+nums[i-1]
    for i in range(n):
        lower=max(0,i-k)
        upper=min(n-1,i+k)
        subarray_sum = cum_sum[upper + 1] - cum_sum[lower]
        subarray_length = upper - lower + 1
        if subarray_length < 2 * k + 1:
            avgs[i] = -1
            continue
        average = subarray_sum // subarray_length
        avgs[i] = average
    return avgs
    
if __name__=="__main__":
    nums = [7,4,3,9,1,8,5,2,6]
    k = 3
    res=getAverages(nums,k)
    print(res)
    print(nums)