def erinevad_sümbolid(sõna):
    hulk=set()
    for i in sõna:
        if i not in hulk:
            hulk.add(i)
    print(hulk)
    return hulk
def sümbolite_sagedus(sõna):
     sõnastik={}
     for i in sõna:
         if i in sõnastik:
             sõnastik[i]=sõnastik[i]+1
         elif i not in sõnastik:
             sõnastik[i]=1
     print(sõnastik)
     return sõnastik
def grupeeri(sõna):
    grupp={}
    grupp["Täishäälikud"]=set()
    grupp["Kaashäälikud"]=set()
    grupp["Muud"]=set()
    for i in sõna:
        if i in ['a','e','i','o','u','õ','ä','ö','ü','A','E','I','O','U','Õ','Ä','Ö','Ü']:
           kordus=sõna.count(i)
           grupp["Täishäälikud"].add((i, kordus ))
        elif i in ['b','c','d','f','g','h','j','k','l','m','n','q','p','r','s','š','z','ž','t','v','w','x','y','B','C','D','F','G','H','J','K','L','M','N','Q','P','R','S','Š','Z','Ž','T','V','W','X','Y']:
            kordus=sõna.count(i)
            grupp["Kaashäälikud"].add((i,kordus ))
        else:
            kordus=sõna.count(i)
            grupp["Muud"].add((i, kordus))
    print(grupp)
    return grupp
    
sõna=input("Sisesta sõna:")
erinevad_sümbolid(sõna)
sümbolite_sagedus(sõna)
grupeeri(sõna)
