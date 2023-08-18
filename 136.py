def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result=0
    for num in nums:
        result^=num
    return result
        
                
if __name__=="__main__":
    nums = [4,1,2,1,2]
    res=singleNumber(nums)
    print(res)