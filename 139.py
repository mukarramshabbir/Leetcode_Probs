def wordBreak( s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # An empty string is always valid

    for i in range(1, n + 1):
        for word in wordDict:
            if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
                break
    
    return dp[n]

if __name__=="__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    result = wordBreak(s,wordDict)
    print(result)