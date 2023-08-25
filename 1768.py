def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    merged=[]
    len1,len2=len(word1),len(word2)
    i,j=0,0
    while i<len1 or j<len2:
        if i<len1:
            merged.append(word1[i])
            i+=1
        if j<len2:
            merged.append(word2[j])
            j+=1
    return ''.join(merged)
    
    

if __name__=="__main__":
    word1 = "ab"
    word2 = "pqrs"
    result = mergeAlternately(word1,word2)
    print(result)