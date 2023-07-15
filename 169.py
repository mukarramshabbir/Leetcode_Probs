def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count=0
    candidate=None
    for i in nums:
        if(count==0):
            candidate=i
            count=1
        if(candidate==i):
            count+=1
        else:
            count-=1
    return candidate
    
if __name__=="__main__":
    nums = [3,2,3]
    res=majorityElement(nums)
    print(res)