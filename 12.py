def intToRoman(num):
    roman=''
    
    sym=[[1000,"M"],[500,"D"],[100,"C"],[50,"L"],[10,"X"],[5,"V"],[1,"I"],]
    for i in range(len(sym)):
        while num>=sym[i][0]:
            roman+=sym[i][1]
            num-=sym[i][0]
    
    
            
    return roman

            
if __name__=="__main__":
    s = 58
    result = intToRoman(s)
    print(result) 