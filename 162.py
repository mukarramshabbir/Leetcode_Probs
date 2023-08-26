def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[mid + 1]:
            # If the middle element is greater than its right neighbor,
            # a peak might exist in the left half, including the middle element.
            right = mid
        else:
            # If the middle element is not greater than its right neighbor,
            # a peak might exist in the right half, excluding the middle element.
            left = mid + 1
            
    # At this point, left and right will converge to a peak element.
    # Both left and right indices will point to the same peak element.
    return left
    
if __name__=="__main__":
    numbers = [2,7,11,15]
    target = 9
    res=twoSum(numbers,target)
    print(res)