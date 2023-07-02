def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    bracket_map={')':'(','}':'{',']':'['}
    
    for c in s:
        if c in ['(','{','[']:
            stack.append(c)
        else:
            if not stack:
                return False
            top=stack.pop()
            if top!=bracket_map[c]:
                return False
    return len(stack)==0
    

if __name__=="__main__":
    s = "()[]{}"
    result = isValid(s)
    print(result)