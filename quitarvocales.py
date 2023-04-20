"""
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels 
from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a 
new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become 
"Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
"""

def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u",
            "A", "E", "I", "O", "U"]
    no_vowels = ""
    for i in string_:
        if i not in vowels:
            no_vowels += i

    return no_vowels

# otra solucion
def disemvowel_2(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

# otra solucion
def disemvowel_3(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


if __name__ == "__main__":

    frase = "This website is for losers LOL!"

    print(disemvowel_3(frase))