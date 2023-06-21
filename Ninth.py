def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if(x<0):
        return False
    x=str(x)

    for i in range(0,len(x)//2):
        if (int(x[i])!=int(x[-(i+1)])):
            return False
    return True
    
    
            
if __name__=="__main__":
    x = 12121
    result = isPalindrome(x)
    print(result) 