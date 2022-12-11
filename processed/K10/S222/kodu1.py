def erinevad_sümbolid(s):
    sõnastik = []
    for täht in s:
        if täht not in sõnastik:
            sõnastik.append(täht)
    return set(sõnastik)

def sümbolite_sagedus(s):
    sõnastik = {}
    for täht in s:
        if täht not in sõnastik:
            sõnastik[täht] = 1
        else:
            sõnastik[täht] += 1
    return sõnastik

def grupeeri(s):
    täishäälikud = {}
    kaashäälikud = {}
    muud = {}
    for täht in s:
        if täht.lower() in ["a","e","i","o","u","õ","ä","ö","ü"]:
            if täht not in täishäälikud:
                täishäälikud[täht] = 1
            else:
                täishäälikud[täht] += 1
        elif täht.lower() in ["q","w","r","t","y","p","s","š","d",
                              "f","g","h","j","k","l"
                              ,"z","ž","x","c","v","b","n","m"]:
            if täht not in kaashäälikud:
                kaashäälikud[täht] = 1
            else:
                kaashäälikud[täht] += 1
        else:
            if täht not in muud:
                muud[täht] = 1
            else:
                muud[täht] += 1
    return {"Täishäälikud":täishäälikud,"Kaashäälikud":kaashäälikud,"Muud":muud}
