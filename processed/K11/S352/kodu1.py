def seosta_lapsed_ja_vanemad(lapsed,nimed):
    f1=open(lapsed,"r")
    f2=open(nimed,"r")

    ik_nimi={}
    laps_vanemad={}

    for rida in f2:
        a=rida.split(" ",1)
        ik_nimi[a[0]]=a[1].strip()
        
    for rida in f1:
        a=rida.split()
        if ik_nimi[a[1]] in laps_vanemad:
            laps_vanemad[ik_nimi[a[1]]]={laps_vanemad.get(ik_nimi[a[1]]),ik_nimi[a[0]]}
        else:
            laps_vanemad[ik_nimi[a[1]]]=ik_nimi[a[0]]
    
    f1.close()
    f2.close()
            
    # Lisasin, kuna automaatkontroll nõudis mingil põhjusel, et vanemad oleks esitatud hulgana :/
    for el in laps_vanemad:
        if type(laps_vanemad[el])!=set:
            laps_vanemad[el]=set([laps_vanemad[el]])
    
    return laps_vanemad

vanemad=seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
print(vanemad)
for laps in vanemad:
    print(laps+": "+ str(vanemad[laps]))