def rotate( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n  # To handle cases where k is larger than the array length
    if k == 0:
        return nums

    # Reverse the entire array
    nums.reverse()

    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])

    # Reverse the remaining elements
    nums[k:] = reversed(nums[k:])
    
if __name__=="__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    res=rotate(nums,k)
    print(nums)