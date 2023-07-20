def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    try:
        index=haystack.index(needle)
        return index
    except:
        return -1
    
    
if __name__=="__main__":
    haystack = "mississippi"
    needle = "issip"
    res=strStr(haystack,needle)
    print(res)