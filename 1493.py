def longestSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    left, right = 0, 0  # Sliding window pointers
    max_length = 0  # Maximum length of subarray containing only 1's
    zero_count = 0  # Count of zeros in the current window

    while right < n:
        if nums[right] == 0:
            zero_count += 1

        # Shrink the window by moving the left pointer if the window contains more than one zero
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update the maximum length of the subarray containing only 1's
        max_length = max(max_length, right - left)

        right += 1

    # If all elements in the array are 1's, return the length of the array - 1 (after removing one element)
    if max_length == n:
        return max_length - 1

    return max_length


            
    

if __name__=="__main__":
    nums = [1,1,0,1]
    result = longestSubarray(nums)
    print(result)