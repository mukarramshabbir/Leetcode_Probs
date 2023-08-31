def convertToTitle(columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """
    result = []

    while columnNumber > 0:
        columnNumber -= 1
        remainder = columnNumber % 26
        result.append(chr(65 + remainder))  # ASCII value of 'A' is 65
        columnNumber //= 26
        
    return ''.join(result[::-1])
    
if __name__=="__main__":
    nums = 701
    res=convertToTitle(nums)
    print(res)