def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zeropointer=0
    for non_zeropointer in range(len(nums)):
        if nums[non_zeropointer]!=0:
            nums[zeropointer],nums[non_zeropointer]=nums[non_zeropointer],nums[zeropointer]
            zeropointer+=1

if __name__=="__main__":
    nums = [0,1,0,3,12]
    result = moveZeroes(nums)
    print(nums)