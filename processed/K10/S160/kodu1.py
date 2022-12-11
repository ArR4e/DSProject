# Teksti analüüs
from collections import Counter

def erinevad_sümbolid(x):
    s = set(x)
    return s

def sümbolite_sagedus(x):
    s = Counter(x)
    return s
        
def grupeeri(x):
    x = x.casefold()
    count1 = {}.fromkeys(Täishäälikud, 0)
        
    for taht in x:
        if taht in count1:
            count1[taht] += 1
        # Kui sellist tähte pole lauses, siis eemaldan
        if (taht in count1) == False:
            ...
            #del count1[]
            
    count2 = {}.fromkeys(Kaashäälikud, 0)
    for letter in x:
        if letter in count2:
            count2[letter] += 1
        # Kui sellist tähte pole lauses, siis eemaldan
        if (letter in count2) == False:  
           ...
            #del count2[]
    
    return count1, count2
    
Täishäälikud = ("aeiuõüäöAEIOUÕÜÄÖ")
Kaashäälikud = ("qwrtypsdfghjklmnbvcxzžQWRTYPSDFGHJKLMNBVCXZŽ")
    
k = grupeeri("Hei hopsti, väikevend!")
print(k)

    