def erinevad_sümbolid(sõne):
    return(set(sõne))
def sümbolite_sagedus(sõne):
    hulk=set(sõne)
    uushulk={}
    for täht in hulk:
        uushulk[täht]=sõne.count(täht)
    return(uushulk)
def grupeeri (sõne):
    täis="AEIOUÕÄÖÜaeiouõäöü"
    kaas="BCDFGHJKLMNPQRSŠZŽTVWXYbcdfghjklmnpqrsšzžtvwxy"
    hulk=set(sõne)
    täishäälikud=set()
    kaashäälikud=set()
    muud=set()
    vastus={}
    for täht in hulk:
        if täht in täis:
            täishäälikud.add((täht,sõne.count(täht)))
        elif täht in kaas:
            kaashäälikud.add((täht,sõne.count(täht)))
        else:
            muud.add((täht,sõne.count(täht)))
    vastus["Täishäälikud"]=täishäälikud
    vastus["Kaashäälikud"]=kaashäälikud
    vastus["Muud"]=muud
    return(vastus)