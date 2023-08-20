def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left,right=0,len(nums)-1
    while left<right:
        mid=left+(right-left)//2
        if nums[mid]>nums[right]:
            left=mid+1
        else:
            right=mid
    return nums[left]
    
if __name__=="__main__":
    nums = [3,2,3]
    res=findMin(nums)
    print(res)