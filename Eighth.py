def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip()
    if not s:
        return 0

    sign = 1
    if s[0] == '-' or s[0] == '+':
        if s[0] == '-':
            sign = -1
        s = s[1:]

    result = 0
    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)

    result = max(-2 ** 31, min(result * sign, 2 ** 31 - 1))
    return result
    
            
if __name__=="__main__":
    x = '-00123  '
    result = myAtoi(x)
    print(result) 