def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]  # Initialize max_sum with the first element
    current_sum = nums[0]  # Initialize current_sum with the first element
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)  # Update current_sum either by taking the current element or adding it to the previous subarray
        max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum becomes greater
        
    return max_sum

if __name__=="__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res=maxSubArray(nums)
    print(res)