def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i=0
    for num in nums:
        if num!=val:
            nums[i]=num
            i+=1
    return i
    
if __name__=="__main__":
    nums = [3,2,2,3]
    val = 3
    res=removeElement(nums,val)
    print(res)
    print(nums)