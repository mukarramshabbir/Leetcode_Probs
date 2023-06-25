def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix=strs[0]
    for string in strs[1:]:
        while(string[:len(prefix)]!=prefix):
            prefix=prefix[:-1]
            if not prefix:
                return ''
    return prefix

if __name__=="__main__":
    strs = ["flower","flow","flight"]
    result = longestCommonPrefix(strs)
    print(result)