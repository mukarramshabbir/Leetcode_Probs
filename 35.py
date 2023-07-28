def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left,right=0,len(nums)-1
    while left<=right:
        mids=left+(right-left)//2
        if nums[mids]==target:
            return mids
        elif nums[mids]<target:
            left=mids+1
        else:
            right=mids-1
    return left
    
if __name__=="__main__":
    nums = [1,3,5,6]
    target = 5
    res=searchInsert(nums,target)
    print(res)