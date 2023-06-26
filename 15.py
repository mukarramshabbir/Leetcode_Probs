def threeSum( nums):
    nums.sort()  # Sort the array in ascending order
    result = []
    for i in range(len(nums) - 2):
        # Skip duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                # Found a triplet that sums to zero
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicate values for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result
    
    

if __name__=="__main__":
    nums = [-1,0,1,2,-1,-4]
    result = threeSum(nums)
    print(result)