def erinevad_sümbolid(sõne):
    tähed=list(sõne)
    hulk=set()
    for i in tähed:
        hulk.add(i)
    return hulk
erinevad_sümbolid('kana')

def sümbolite_sagedus(sõne):
    tähed=list(sõne)
    sõnastik={}
    for i in tähed:
        sõnastik[i]=0
    for i in tähed:
        if i in sõnastik:
            sõnastik[i]=sõnastik[i]+1
    return sõnastik

sümbolite_sagedus("kana on hoos")

täishäälikud=('a','e','i','o','u','õ','ä','ö','ü')
kaashäälikud=('l','m','n','r','s','v','h','j','p','b','t','d','k','g')
def grupeeri(sõne):
     sõnastik1={}
     sõnastik1["Täishäälik"]=set()
     sõnastik1["Kaashäälik"]=set()
     sõnastik1["Muud"]=set()
     sõnastik2=sümbolite_sagedus(sõne)
     for i in sõnastik2:
         if i.lower() in täishäälikud:
             sõnastik1["Täishäälik"].add((i,sõnastik2[i]))
         elif i.lower() in kaashäälikud:
             sõnastik1["Kaashäälik"].add((i,sõnastik2[i]))
         else:
             sõnastik1["Muud"].add((i,sõnastik2[i]))
     return sõnastik1
grupeeri("Hei-hei")              