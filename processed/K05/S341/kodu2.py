import string

a= input("Sisestage lause:")
def suurväike():
    global a
    
    swapped_string=""
    swapped_string += a.swapcase()
    for string.punctuation in swapped_string:
        if string.punctuation in swapped_string:
            final_swapped_string= a.translate(str.maketrans(''&'',string.punctuation))

print(str(suurväike()))
