import re
def isPalindrome( s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase and remove non-alphanumeric characters
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
        # Check if the cleaned string is equal to its reverse
        return cleaned_s == cleaned_s[::-1]
    
if __name__=="__main__":
    s = "A man, a plan, a canal: Panama"
    result = isPalindrome(s)
    print(result)