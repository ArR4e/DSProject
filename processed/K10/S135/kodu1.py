def erinevad_sümbolid(word):
    return set(word)

def sümbolite_sagedus(word):
    n = {}
    chars = []
    for char in word:
        if char in chars:
            continue
        n[char] = word.count(char)
        chars.append(char)
    return n

def grupeeri(word):
    n = {}
    chars = []
    tais = set()
    kaas = set()
    muu = set()
    for char in word:
        if char in chars:
            continue
        if char.isalpha():
            if char.lower() in ['a','e','i','o','u','õ','ü','ö','ä']:
                tais.add((char, word.count(char)))
            else:
                kaas.add((char, word.count(char)))
        else:
            muu.add((char, word.count(char)))
    n['Täishäälikud'] = tais
    n['Kaashäälikud'] = kaas
    n['Muud'] = muu
    return n
            
