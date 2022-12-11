def erinevad_sümbolid(sõnad):return set(sõnad)
def sümbolite_sagedus(sõnad):
    sõnastik = {}
    for täht in sõnad:
        try:
            if sõnastik[täht] >= 1:
                sõnastik.update({täht:(sõnastik[täht]+1)})
                continue
        except:
            sõnastik.update({täht:1})          
    return sõnastik
def grupeeri(sõnad):
    täis = set()
    kaas = set()
    muud = set()
    kogu = []
    täishäälikud = ['A','a','E','e','I','i','U','u','O','o','Õ','õ','Ä','ä','Ü','ü','Ö','ö']
    kaashäälikud = [ 'B','b', 'C','c', 'D','d', 'F','f', 'G','g', 'H','h', 'J','j', 'K','k', 'L','l', 'M','m', 'N','n', 'P','p', 'Q','q', 'R','r', 'S','s', 'Š','š', 'Z','z', 'Ž','ž','T','t', 'V','v','W','w','X','x','Y','y']
    for i in range(len(sõnad)):
        a = 0
        for täht in sõnad[i:len(sõnad)]:
            if täht == sõnad[i]:
                a+=1
        rida = (sõnad[i],a)
        kogu+=[rida]
    print(kogu)
    for i in range(len(kogu)):
        for el in(kogu[i+1:len(kogu)]):
            if el[0]==kogu[i][0]:
                kogu.remove(el)
    print(kogu)
    for el in kogu:
        if el[0] in täishäälikud:
            täis.add(el)
        elif el[0] in kaashäälikud:
            kaas.add(el)
        else:
            muud.add(el)
    return {"Täishäälikud":täis,"Kaashäälikud":kaas,'Muud':muud}
# sõne = "sõida tasa üle silla"
# #print(erinevad_sümbolid(sõne))
# #print(sümbolite_sagedus(sõne))
# print(grupeeri(sõne))