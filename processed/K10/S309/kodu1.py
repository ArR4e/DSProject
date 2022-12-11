
def erinevad_sümbolid(string):

    #O(n)
    return set(string)

def sümbolite_sagedus(string):

    dictionary = {}
    keys = erinevad_sümbolid(string)

    for key in keys:
        dictionary[key] = 0

    for letter in string:
        if letter in keys:
            dictionary[letter] += 1

    #O(2n) ehk O(n)
    return dictionary

def grupeeri(string):

    dictionary = {}
    dictionary["Täishäälikud"] = set()
    dictionary["Kaashäälikud"] = set()
    dictionary["Muud"] = set()

    letterdict = sümbolite_sagedus(string)

    for key in letterdict:
        if str(key).lower() in ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]:
            dictionary["Täishäälikud"].add(((key, letterdict[key])))
        elif str(key).lower() in ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "y"]:
            dictionary["Kaashäälikud"].add(((key, letterdict[key])))
        else:
            dictionary["Muud"].add(((key, letterdict[key])))

    #vist O(n + 30n) ehk O(n)
    return dictionary