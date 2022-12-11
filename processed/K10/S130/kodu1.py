#teksti analüüs

def erinevad_sümbolid(sõne):
    leitud = set(sõne)& set(sõne)
    return leitud

#print(erinevad_sümbolid('hulk ei sisalda kunagi korduvaid elemente'))

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        sõnastik[el] = sõnastik.get(el, 0) + 1
    return sõnastik

#print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    a = {'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü', 'a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü'}

    b = {'x', 'c', 'q', 'y', 'w', 'h', 'j', 'l', 'm', 'n', 'r', 's', 't', 'v', 'k', 'p', 'g', 'b', 'd', 'f', 'š', 'z', 'ž',
        'X', 'C', 'Q', 'Y', 'W', 'H', 'J', 'L', 'M', 'N', 'R', 'S', 'T', 'V', 'K', 'P', 'G', 'B', 'D', 'F', 'Š', 'Z', 'Ž'}
    
    kui_palju = sümbolite_sagedus(sõne)
    #c = sõne.lower()
    taishaalikud = set()
    kaashaalikud = set()
    muud = set()
    tähed = {}
    
    for el in sõne:
        if el in a:
            taishaalikud.add((el, kui_palju[el]))
        
        elif el in b:
            kaashaalikud.add((el, kui_palju[el]))
        else:
            muud.add((el, kui_palju[el]))

#Proovisin viimast Fail'i parandada sellega, et juhul kui täis-, kaashäälikuid või muid sümboleid ei ole selle asendada mingi lausega... tuli veelgirohkem Fail'e
#            if taishaalikud == set():
#                taishaalikud = 'Täishäälikuid ei ole'
#            elif kaashaalikud == set():
#                kaashaalikud = 'Kaashäälikuid ei ole'
#            elif muud == set():
#                muud = 'Muid märke ei ole'

# Ka viimase Fail'i pärast... Aga kontrollile ei meeldinud, et kui teiste lausete juures, kus ei olnud ühte kategooriat, jäi see lõpptulemusest välja.
#         if taishaalikud != set():
#             tähed['Täishäälikud'] = taishaalikud
#         if kaashaalikud != set():
#              tähed['Kaashäälikud'] = kaashaalikud
#         if muud != set():
#              tähed['Muud'] = muud

        tähed['Täishäälikud'] = taishaalikud
        tähed['Kaashäälikud'] = kaashaalikud
        tähed['Muud'] = muud
        
    return tähed
#Panin Thonnys sama sõne programmi, mis annab veateadet, ja ma sain vastuseks {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': {("'", 2), ('.', 1)}}
    
            
    
#print(grupeeri("sõida tasa üle silla!"))
#kui_palju = sümbolite_sagedus(sõne)
#     Täishäälikud =  kui_palju ^ a
#     Kaashäälikud = kui_palju ^ b
#     Muud = kui_palju - Täishäälikud - Kaashäälikud
#     print(Muud)
#     print(Kaashäälikud)
#     print(Täishäälikud)
        