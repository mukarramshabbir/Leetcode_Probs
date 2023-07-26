def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if(n==0):
        return 1
    elif(n<0):
        x=1/x
        n=-n
    result=1
    while n>0:
        if n%2==1:
            result*=x
        x*=x
        n//=2
    return result

    
if __name__=="__main__":
    x = 2.00000
    n = 10
    res=myPow(x,n)
    print(res)