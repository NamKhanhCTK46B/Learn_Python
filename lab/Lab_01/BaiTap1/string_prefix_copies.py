def substring_copy (text, n):
    flen = 2

    if flen > len(text):
        flen = len(text)
    
    substr = text [:flen]

    result = ""

    for i in range (n):
        result = result + substr
    
    return result

print(substring_copy('abcdef', 2)) 
print(substring_copy('p', 3)) 