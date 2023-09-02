def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    max_products=nums[0]
    min_products=nums[0]
    result=nums[0]
    
    for i in range(1,len(nums)):
        if nums[i]<0:
            max_products,min_products=min_products,max_products
        max_products=max(nums[i],max_products*nums[i])
        min_products=min(nums[i],min_products*nums[i])
        
        result=max(result,max_products)
    return result
    
if __name__=="__main__":
    nums = [2,3,-2,4]
    res=maxProduct(nums)
    print(res)