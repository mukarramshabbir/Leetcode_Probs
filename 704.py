def peakIndexInMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    left,right=0,len(arr)-1
    while(left<right):
        mid=left+(right-left)//2
        if(arr[mid]>arr[mid+1]):
            right=mid
        else:
            left=mid+1
    return left

if __name__=="__main__":
    arr = [0,10,5,2]
    res=peakIndexInMountainArray(arr)
    print(res)