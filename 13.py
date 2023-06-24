def romanToInt(s):
    symbol_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    prev = 0
    
    for i in range(len(s) - 1, -1, -1):
        curr = symbol_values[s[i]]
        if curr < prev:
            result -= curr
        else:
            result += curr
            prev = curr
    
    return result


            
if __name__=="__main__":
    s = 'MCMXCIV'
    result = romanToInt(s)
    print(result) 