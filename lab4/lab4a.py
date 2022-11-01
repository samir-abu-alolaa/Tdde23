
import string
lowercase = string.ascii_lowercase+"åäö" # alla gemener 
uppercase = string.ascii_uppercase+"ÅÄÖ" # alla versaler
case1 = lowercase+"_"+"." # första fallet 
case2 = uppercase+ " " + "|" # andra fallet

def split_rec(str):

    if not str:
        return ("", "") # om det är inte en string retunera töm
    
    c = str[0] # första element i stringen 
    res1, res2 = split_rec(str[1:]) # res1 och res2 är lika med element förutom det första
    res1 = c+res1 if c in case1 else res1 # om första elementet ingår i fall ett så läggas det till res1 annars res2
    res2 = c+res2 if c in case2 else res2
    return res1, res2

def split_it(str):
    
    str1 = str2 = "" 
    for char in str: # för alla element i string
        if char in case1: # om element ingår i fall1 läggas det till str1
            str1+= char
        if char in case2: # om element ingår i fall2 läggas det till str2
            str2+= char
    return (str1, str2)