def erinevad_sümbolid(string):
    hulk = set()
    for i in string:
        hulk.add(i)
    return hulk
            
def sümbolite_sagedus(string):
    dictionary = {}
    for i in string:
        if i not in dictionary.keys():
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary

def grupeeri(string):
    täishäälikud = "aeiouõäöü"
    täishäälikud_L = täishäälikud.upper()
    kaashäälikud = "bdfghjklmnprsztvžšqywxc"
    kaashäälikud_L = kaashäälikud.upper()
    dictionary = {"Täishäälikud":set(), "Kaashäälikud":set(), "Muud":set()}
    for i in string:
        if i in täishäälikud or i in täishäälikud_L and (i, string.count(i)) not in dictionary["Täishäälikud"]:
            count = string.count(i)
            dictionary["Täishäälikud"].add((i, count))    
        elif i in kaashäälikud or i in kaashäälikud_L and (i, string.count(i)) not in dictionary["Kaashäälikud"]:
            count = string.count(i)
            dictionary["Kaashäälikud"].add((i, count))
        elif i not in täishäälikud and i not in kaashäälikud and i not in täishäälikud_L and i not in kaashäälikud_L and (i, string.count(i)) not in dictionary["Muud"]:
            count = string.count(i)
            dictionary["Muud"].add((i, count))
    return dictionary





            
        
    


            
            