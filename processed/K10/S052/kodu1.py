def erinevad_sümbolid(string):
    symbols = list(string)
    diff_symbols = []
    for each in symbols:
        if not each in diff_symbols:
            diff_symbols.append(each)
        else:
            continue
    return diff_symbols

def sümbolite_sagedus(string):
    symbols = list(string)
    diff_symbols = erinevad_sümbolid(string)

    counted_symbols = {}
    for each in diff_symbols:
        väärtus = string.count(each)
        counted_symbols[each] = väärtus
    return counted_symbols


def grupeeri(string):
    default_vowels = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
    vowels = {}
    consonants = {}
    rest = {}
    final = {}
    counted_symbols = sümbolite_sagedus(string)
    for key in counted_symbols:
        value = counted_symbols[key]
        if key.lower() in default_vowels:
            vowels[key] = value
        elif key.isalpha():
            consonants[key] = value
        else:
            rest[key] = value
        
    final['Täishäälikud:'] = vowels
    final['Kaashäälikud:'] = consonants
    final['Muu:'] = rest
    return(final)
            
    
grupeeri("sõida tasa üle silla")