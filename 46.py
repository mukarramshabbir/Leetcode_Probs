def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])  # Add a copy of the current permutation to the result
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap elements
            backtrack(start + 1)  # Recurse with the next position
            nums[start], nums[i] = nums[i], nums[start]  # Swap back to backtrack
            
    result = []
    backtrack(0)  # Start the backtracking process
    return result

if __name__=="__main__":
    nums = [1,2,3]
    res=permute(nums)
    print(res)