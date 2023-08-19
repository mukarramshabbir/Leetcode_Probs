def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    words=s.strip().split()
    if words:
        return len(words[-1])
    else:
        return 0
    
if __name__=="__main__":
    s = "Hello World"
    res=lengthOfLastWord(s)
    print(res)