def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    n=len(digits)
    carry=1
    for i in range(n-1,-1,-1):
        total=digits[i]+carry
        digits[i]=total%10
        carry=total//10
    if carry:
        digits.insert(0,carry)
    return digits

if __name__=="__main__":
    nums = [4,3,2,1]
    result = plusOne(nums)
    print(result)