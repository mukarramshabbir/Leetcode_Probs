def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    count=0
    i=0
    while i<len(flowerbed):
        if(flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0)):
            flowerbed[i]=1
            count+=1
        if(count>=n):
            return True
        i+=1
    return False
    
if __name__=="__main__":
    flowerbed = [1,0,0,0,1]
    n = 2
    res=canPlaceFlowers(flowerbed,n)
    print(res)