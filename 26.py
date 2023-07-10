def buddyStrings(s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    if(len(s)!=len(goal)):
        return False
    if(s==goal):
        seen=set()
        for i in s:
            if i in seen:
                return True
            seen.add(i)
        return False
    mismatch=[]
    for i in range(len(s)):
        if(s[i]!=goal[i]):
            mismatch.append(i)
    return len(mismatch)==2 and s[mismatch[0]]==goal[mismatch[1]] and s[mismatch[1]]==goal[mismatch[0]]
    



    
if __name__=="__main__":
    s = "ab"
    goal = "ab"
    res=buddyStrings(s,goal)
    print(res)