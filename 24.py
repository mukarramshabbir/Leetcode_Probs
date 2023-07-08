def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    # Initialize two pointers: i for iterating the array, and j for tracking the last unique element
    i = 1
    j = 0

    while i < len(nums):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j + 1


    
if __name__=="__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    res=removeDuplicates(nums)
    print(res)
    print(nums)