def erinevad_sümbolid(a):
    return set(a)

def sümbolite_sagedus(a):
    di = {}
    for i in a:
        di[i] = di.get(i, 0) + 1
    return di

def grupeeri(a):
    vowels = ('a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü',
              'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü')
    consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y',
                  'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
                  'P', 'Q', 'R', 'S', 'Š', 'Z', 'Ž', 'T', 'V', 'W', 'X', 'Y')
    di = {}
    vowel_set = set()
    consonant_set = set()
    other_set = set()
    for i in a:
        if i in vowels:
            vowel_set.add((i, sümbolite_sagedus(a)[i]))
        elif i in consonants:
            consonant_set.add((i, sümbolite_sagedus(a)[i]))
        else:
            other_set.add((i, sümbolite_sagedus(a)[i]))
    di['Täishäälikud'] = vowel_set
    di['Kaashäälikud'] = consonant_set
    di['Muud'] = other_set
    return di