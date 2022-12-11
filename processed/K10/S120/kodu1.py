vowels = 'aeiouõäöü'
consonants = 'bcdfghjklmnpqrsšzžtvwxyz'

def erinevad_sümbolid(inStr):
    return set(inStr)


def sümbolite_sagedus(inStr):
    char_dict = {}
    char_set = erinevad_sümbolid(inStr)
    for char in char_set:
        char_dict[char] = inStr.count(char)

    return char_dict

def grupeeri(inStr):
    grouped_dict = {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    freq_dict = sümbolite_sagedus(inStr)
    for char in freq_dict:
        target = 'Muud'
        if char.lower() in vowels:
            target = 'Täishäälikud'
        elif char.lower() in consonants:
            target = 'Kaashäälikud'
        else:
            target = 'Muud'
        grouped_dict[target].add((char, freq_dict[char]))

    return grouped_dict

print(grupeeri("sõida tasa üle silla"))
