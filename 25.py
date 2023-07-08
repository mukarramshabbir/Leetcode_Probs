def minSubarrayLength(target,nums):
    
    
    n = len(nums)
    left = 0
    min_length = float('inf')
    current_sum = 0

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0



    
if __name__=="__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    res=minSubarrayLength(target,nums)
    print(res)