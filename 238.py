def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    answer = [1] * n
    
    # Calculate products of elements to the left of each element
    left_product = 1
    for i in range(n):
        left_products[i] = left_product
        left_product *= nums[i]
    # Calculate products of elements to the right of each element
    right_product = 1
    for i in range(n - 1, -1, -1):
        right_products[i] = right_product
        right_product *= nums[i]
    # Multiply left and right products element-wise to get the final answer
    for i in range(n):
        answer[i] = left_products[i] * right_products[i]
    
    return answer

if __name__=="__main__":
    nums = [1,2,3,4]
    res=productExceptSelf(nums)
    print(res)