def erinevad_sümbolid(sõne):
    hulk=set()
    for sümbol in sõne:
        hulk.add(sümbol)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik={}
    for sümbol in sõne:
        sõnastik[sümbol]=sõnastik.get(sümbol,0)+1
    return sõnastik

def grupeeri(sõne):
    täishäälikud="AaEeIiOoUuÕõÄäÖöÜü"
    kaashäälikud="BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy"
    sõnastik={}
    tharv=set()
    kharv=set()
    muud=set()
    for sümbol in sõne:
        if sümbol in täishäälikud:
            tharv.add((sümbol, sõne.count(sümbol)))
        elif sümbol in kaashäälikud:
            kharv.add((sümbol, sõne.count(sümbol)))
        else:
            muud.add((sümbol, sõne.count(sümbol)))
    sõnastik["Täishäälikud"]=tharv
    sõnastik["Kaashäälikud"]=kharv
    sõnastik["Muud"]=muud
    return sõnastik