def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count_dic={}
    for num in nums:
        count_dic[num]=count_dic.get(num,0)+1
    sorted_elements=sorted(count_dic.keys(),key=lambda x: (-count_dic[x],x))
    result = sorted_elements[:k]
    
    return result

if __name__=="__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    result = topKFrequent(nums,k)
    print(result)