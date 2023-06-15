def longestPalindrome(s):
    index=-1
    length=len(s)
    maxlength=0
    for i in range(length):
        for j in range(i,length):
            palindrome=1
            for k in range(0,((j-i)//2)+1):
                if(s[i+k]!=s[j-k]):
                    palindrome=0
            if(palindrome!=0 and j-i+1>maxlength):
                index=i
                maxlength=j-i+1
    return s[index:index+maxlength]
            
if __name__=="__main__":
    s='babad'
    s=longestPalindrome(s)
    print(s)