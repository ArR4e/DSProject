def erinevad_sümbolid(sõne):
    return set(sõne)
print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))
sõnastik={}
def sümbolite_sagedus(sone):
    global sõnastik
    char_count = lambda sone, täht: sone.count(täht)
    sõnastik = dict( [ ( täht, char_count(sone, täht) ) for täht in sone ]  )
    return sõnastik
    
print(sümbolite_sagedus("Hei hopsti, väikevend!"))
s6nastik1 = {}


def grupeeri(s6ne):
    global s6nastik1
    häälik = ["a", "e", "i", "o", "u","õ","ä","ü","ö"]
    s6nastik1[häälik]=set()
    for võti in s6nastik1:
        print(võti)
        print(s6nastik[võti])
    tähe_count= lambda s6ne, t2ht: s6ne.count(t2ht)
    s6nastik1 = dict( [( täishäälikud, tähe_count(s6ne,täishäälikud)) for täishäälikud in s6ne ] )
    return s6nastik1
print(grupeeri("heio, kuidas sul läheb"))