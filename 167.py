def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # Add 1 to indices since they are 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None 
    
if __name__=="__main__":
    numbers = [2,7,11,15]
    target = 9
    res=twoSum(numbers,target)
    print(res)