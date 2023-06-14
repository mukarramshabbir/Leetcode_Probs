def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    print(nums1,nums2)
    m, n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
        partition1 = (low + high) // 2
        partition2 = ((m + n + 1) // 2) - partition1

        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            else:
                return max(maxLeft1, maxLeft2)

        elif maxLeft1 > minRight2:
            high = partition1 - 1
        else:
            low = partition1 + 1

    # Error case
    return -1

        
    
    

        

if __name__=="__main__":
    nums1 = [1,2,8,9]
    nums2 = [3,4,7]
    s=findMedianSortedArrays(nums1,nums2)
    print(s)