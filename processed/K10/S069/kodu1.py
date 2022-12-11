sõne = input('Sisesta lause: ')

def erinevad_sümbolid(sõne):
    vastus = set(sõne)
    return vastus

def sümbolite_sagedus(sõne):
    vastus = {}
    array = list(sõne)
    for el in array:
        j = 0
        for i in range(len(array)):
            if el == array[i]:
                j += 1
        vastus[el] = j
    return vastus
            
    
def grupeeri(sõne):
    thäälikud = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü']
    khäälikud = ['C', 'W', 'Q', 'X', 'Y', 'c', 'w', 'q', 'x', 'y', 'v', 'j', 'l', 'm', 'n', 'r', 's', 'h', 'f', 'g', 'z', 'k', 'b', 'p', 'd', 't', 'V', 'J', 'L', 'M', 'N', 'R', 'S', 'H', 'F', 'G', 'Z', 'K', 'B', 'P', 'D', 'T']
    vastus = {}
    array = list(sõne)
    sõn = sümbolite_sagedus(sõne)
    t = set()
    k = set()
    s = set()
    for el in array:
        if el in thäälikud:
            t.add((el, sõn[el]))
        elif el in khäälikud:
            k.add((el, sõn[el]))
        else:
            s.add((el, sõn[el]))
    vastus['Täishäälikud'] = t
    vastus['Kaashäälikud'] = k
    vastus['Muud'] = s
    return vastus









