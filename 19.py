def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    stack=set()
    for i in nums:
        if i in stack:
            return True
        
        stack.add(i)
    return False 
            
    

if __name__=="__main__":
    prices = [7,1,5,3,6,4]
    result = containsDuplicate(prices)
    print(result)