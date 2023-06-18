def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    rev=0
    neg=False
    if(x<0):
        x=-1*x
        neg=True
    while(x!=0):
        r=x%10
        x=x//10
        if rev > 2147483647 // 10 or (rev == 2147483647 // 10 and r > 7):
            return 0
        rev=rev*10+r
    if(neg==True):
        rev=-1*rev
    return rev
    
            
if __name__=="__main__":
    x = 123
    result = reverse(x)
    print(result) 