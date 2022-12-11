def erinevad_sümbolid(tekst):
    b = set(tekst)
    c = set(list(b))
    return c
def sümbolite_sagedus(tekst):
    b=[]
    for word in range(len(tekst)):
        for letter in tekst[word]:
            if letter[0]=='':
                b.append(None)
            else:
                b.append(letter[0])
            
    sõnastik= {x:b.count(x) for x in b}
    return sõnastik
def grupeeri(tekst):
    uus = {'Täishäälikud' :[] ,'Kaashäälikud' : [] ,'Muud' : []}
    a = tekst.lower()
    b = sümbolite_sagedus(a)
    for võti in b:
        if võti in "aeuioöäõü":
            uus["Täishäälikud"].append(võti+" , "+str(b[võti]))
        elif võti in "bdfghjklmnprsšžzv":
            uus["Kaashäälikud"].append(võti+" , "+ str(b[võti]))
        elif võti in "!?/.,[]||":
            uus["Muud"].append(võti+" , "+ str(b[võti]))
    return(uus)