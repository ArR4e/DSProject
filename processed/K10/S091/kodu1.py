def erinevad_sümbolid(sone):
    hulk = set(sone)
    return hulk

def sümbolite_sagedus(sone):
    sagedus = {}
    for el in sone:
        sagedus[el] = sone.count(el)
    return sagedus
        
def grupeeri(sone):
    sumbolid = sümbolite_sagedus(sone)
    taishaalikud = set()
    taishaalikud1 = ['a','e','u','i','o','ä','ö','ü','õ','A','E','U','I','O','Ä','Ö','Õ','Ü']
    kaashaalikud = set()
    kaashaalikud1 = ['ž','š','q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Ž','Š','Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    muu = set()
    for taht,sagedus in sumbolid.items():
        if taht in taishaalikud1:
            taishaalikud.add(((taht,sagedus)))
        elif taht in kaashaalikud1:
            kaashaalikud.add(((taht,sagedus)))
        else:
            muu.add(((taht,sagedus)))
    grupid = {'Täishäälikud':taishaalikud,'Kaashäälikud':kaashaalikud,'Muud':muu}
    return grupid