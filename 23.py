def merge( nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    k=m+n-1
    m,n=m-1, n-1
    
    
    while m>=0 and n>=0:
        if(nums1[m]>=nums1[n]):
             nums1[k]=nums1[m]
             m-=1
        else:
             nums1[k]=nums2[n]
             n-=1
        k-=1
    while n >= 0:
        nums1[k] = nums2[n]
        n -= 1
        k -= 1
    nums1.sort()

    
if __name__=="__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1,m,nums2,n)
    print(nums1)