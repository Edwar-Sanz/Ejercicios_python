"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

"""


def valid_braces(string):
    val = True
    b1 = 0
    b2 = 0
    b3 = 0

    for i in string:
        if b1<0 or b2<0 or b3<0:
            val = False
            return val
        
        elif i == "(":
            b1 +=1
        elif i == "[":
            b2 +=1
        elif i == "{":
            b3 += 1
        elif i == ")":
            b1 -=1
        elif i == "]":
            b2 -=1
        elif i == "}":
            b3 -= 1
        print(b1, b2, b3, end="\n")
    
    for i in ["(]", "(}", "[)", "[}", "{)", "{]"]:
        if i in string:
            val = False
            return val

    if b1==0 and b2==0 and b3==0:
        return True
    else:
        return False
    


# Solucion:
def validBraces(string):
    for i in range(len(string)//2):
        string = string.replace('{}', '')
        string = string.replace('[]', '')
        string = string.replace('()', '')
    return len(string) == 0



# string = "())({}}{()][]["
# string = "()"  
# string = "([{}])"   
# string = "(}"      
string = "[(])"    
# string = "[({})](]" 

print(valid_braces(string))
