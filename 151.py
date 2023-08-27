def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split()  # Split the input string into words
    reversed_words = reversed(words)  # Reverse the order of words
    result = ' '.join(reversed_words)  # Join the reversed words with a single space
    return result
    
if __name__=="__main__":
    s = "the sky is blue"
    res=reverseWords(s)
    print(res)