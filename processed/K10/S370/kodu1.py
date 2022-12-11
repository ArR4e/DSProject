import string
def erinevad_sümbolid(sõne):
    sümbolid=set(sõne)
    return(sümbolid)
def sümbolite_sagedus(s):
    sagedus={}
    for sümbol in list(s):
        sagedus[sümbol]=sagedus.get(sümbol,0)+1
    return(sagedus)
def grupeeri(s):
    täishäälikud=tuple("AEIOUÕÄÖÜPaeiouõäöü")
    kaashäälikud=tuple(x for x in string.ascii_uppercase+string.ascii_lowercase if x not in täishäälikud)
    täisl={}
    kaasl={}
    muul={}
    for x in list(s):
        if x in täishäälikud:
            täisl[x]=täisl.get(x,0) +1
        elif x in kaashäälikud:
            kaasl[x]=kaasl.get(x,0) +1
        else:
            muul[x]=muul.get(x,0) +1
    return {'Täishäälikud': set((x,täisl[x]) for x in täisl), 'Kaashäälikud': set((x,kaasl[x]) for x in kaasl), 'Muud' : set((x,muul[x]) for x in muul)}