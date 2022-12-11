a="SõõÄÄÄÄÄÄ tasa üle silla"
def erinevad_sümbolid(a):
    return set(a)

def sümbolite_sagedus(a):
    e=[]
    sagedus={}
    for rida in a:
        e.append(rida)
    for i in e:
        sagedus[i]=e.count(i)
    return sagedus
def grupeeri(a):
    grupp={}
    e=[]
    sagedus={}
    täishäälikud=set()
    kaashäälikud=set()
    muud=set()
    for rida in a:
        rida=rida.lower()
        e.append(rida)
    for i in e:
        sagedus[i]=e.count(i)
    for rida in a:
        rida=rida.lower()
        if rida in ('a','e','i','o','u','õ','ä','ö','ü'):
            ennik=(rida, sagedus[rida])
            täishäälikud.add(ennik)
        elif rida in ('b','d','c','h','j','k','l','n','m','p','q','r','s','t','v','w','š','z','ž','x','y','g'):
            ennik=(rida, sagedus[rida])
            kaashäälikud.add(ennik)
        else:
            ennik=(rida, sagedus[rida])
            muud.add(ennik)
    grupp['Täishäälikud']=täishäälikud
    grupp['Kaashäälikud']=kaashäälikud
    grupp['Muud']=muud
    return grupp