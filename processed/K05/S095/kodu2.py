import random
import string
random = random.choice(string.punctuation)
tekst=input("Sisesta mingi lause: ")

def suurväike(tekst):
    suursõna=''
    for suur in tekst:
        if suur.isupper():
            suursõna+=suur.lower()
        if suur.islower():
            suursõna+=suur.upper()
        if suur.isspace():
            suursõna+=' '
        if suur in string.punctuation:
            suursõna+=random
    print(suursõna)
suurväike(tekst)

# https://www.geeksforgeeks.org/string-punctuation-in-python/
# https://www.geeksforgeeks.org/python-string-isspace-method/
# https://pynative.com/python-generate-random-string/
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.programiz.com/python-programming/methods/string/upper
# https://www.w3schools.com/python/ref_string_islower.asp
# https://careerkarma.com/blog/python-lowercase/
# https://careerkarma.com/blog/python-uppercase/
