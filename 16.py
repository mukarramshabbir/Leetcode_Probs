def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    n=len(nums)
    closestSum=float('inf')
    
    for i in range(n-2):
        left=i+1
        right=n-1
        
        while(left<right):
            currentSum=nums[i]+nums[left]+nums[right]
            if abs(currentSum-target)<abs(closestSum-target):
                closestSum=currentSum
            if currentSum<target:
                left+=1
            elif currentSum>target:
                right-=1
            else:
                return target
    return closestSum
    
    

if __name__=="__main__":
    nums = [-1,2,1,-4]
    target = 1
    result = threeSumClosest(nums,target)
    print(result)