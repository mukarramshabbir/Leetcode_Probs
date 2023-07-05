def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!= len(t)):
            return False
        for i in s:
            if i not in t:
                return False
            else:
                t=t.replace(i,"",1)
        return True
            
    

if __name__=="__main__":
    s = "anagram"
    t = "nagaram"
    result = isAnagram(s,t)
    print(result)