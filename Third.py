def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    seen={}
    start=0
    max_length=0
    for end in range(len(s)):
        if(s[end] in seen and start<=seen[s[end]]):
            start=seen[s[end]]+1
        else:
            max_length=max(max_length,end-start+1)
        seen[s[end]]=end
    print(max_length)
    return max_length
    
    

        

if __name__=="__main__":
    s=lengthOfLongestSubstring('abcabcbb')