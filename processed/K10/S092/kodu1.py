# https://courses.cs.ut.ee/2021/programmeerimine/fall/Main/Kodu10
# https://progeopik.cs.ut.ee/10_andmestruktuurid.html
vowels = ["A", "E", "I", "O", "U", "Õ", "Ä", "Ö", "Ü"]
consonants = ["B", "G", "F", "D", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "V", "X", "Y", "Z", "W", "C", "Q"]

def mk_set(arg):
    el_set = set()
    for el in arg:
        tuple_el = (el, arg[el])
        el_set.add(tuple_el)
    return el_set

def ch_set(arg, ch):
    try:
        arg[ch] += 1
    except:
        arg[ch] = 1
    return arg

# 0 - muud, 1 - täishäälik, 2 - kaashäälik
def ch_type(arg):
    try:
        arg = arg.upper()
        if arg in vowels:
            return 1
        #elif arg in c:
        elif arg in consonants:
            return 2
        else:
            return 0
    except:
        return 0

def erinevad_sümbolid(arg):
    symbols = set()
    for ch in arg:
        symbols.add(ch)
    return symbols
    
def sümbolite_sagedus(arg):
    symbols = {}
    for ch in arg:
        try:
            symbols[ch] += 1
        except:
            symbols[ch] = 1
    return symbols
    
def grupeeri(arg):
    #sym = {"Täishäälikud", "Kaashäälikud", "Muud"}
    sym = {}
    muud = {}
    täishäälikud = {}
    kaashäälikud = {}
    for ch in arg:
        ch_t = ch_type(ch)
        if ch_t == 0:
            ch_set(muud, ch)
        elif ch_t == 1:
            ch_set(täishäälikud, ch)
        else:
            ch_set(kaashäälikud, ch)

    sym["Muud"] = mk_set(muud)
    sym["Täishäälikud"] = mk_set(täishäälikud)
    sym["Kaashäälikud"] = mk_set(kaashäälikud)
    return sym