def erinevad_sümbolid(lause):
    list_tähed = [x for x in lause]
    return set(list_tähed)
    
def sümbolite_sagedus(lause):
    dict_tähed = dict.fromkeys(erinevad_sümbolid(lause),0)
    for x in lause:
        dict_tähed[x] += 1
    return dict_tähed



def grupeeri(lause):
    dict_häälikud = {}
    dict_häälikud['Täishäälikud'] = set()
    dict_häälikud["Kaashäälikud"] = set()
    dict_häälikud["Muud"] = set()
    dict_tähed = sümbolite_sagedus(lause)
    for x in dict_tähed.keys():
        if x in ["i","ü","u","e","ö","õ","o","ä","a"] or x in ["I","Ü","U","E","Ö","Õ","O","Ä","A"]:
            el = (x, dict_tähed[x])
            dict_häälikud["Täishäälikud"].add(el)
        elif x in ["B","b","C","c","D","d","F","f","G","g","H","h","J","j","K","k","L","l","M","m","N","n","P","p","Q","q","R","r","S","s","Š","š","Z","z","Ž","ž","T","t","V","v","W","w","X","x","Y","y"]:
            el = (x, dict_tähed[x])
            dict_häälikud["Kaashäälikud"].add(el)
        else:
            el = (x, dict_tähed[x])
            dict_häälikud["Muud"].add(el)
    return dict_häälikud