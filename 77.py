def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    def backtrack(start,current_combination):
        if len(current_combination)==k:
            result.append(current_combination[:])
            return
        for num in range(start,n+1):
            current_combination.append(num)
            backtrack(num+1,current_combination)
            current_combination.pop()
    result=[]
    backtrack(1,[])
    return result

if __name__=="__main__":
    n = 4
    k = 2
    res=combine(n,k)
    print(res)