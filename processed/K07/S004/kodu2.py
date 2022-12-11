with open("taksohinnad.txt","r",encoding="utf-8") as f:
    tekst=[]
    for x in f:
        x=x.strip()
        tekst.append(x.split(","))
    
teepikkus=float(input("Sisesta teepikkus koju: "))
hindkoju=9**99
odavaimtakso=""
for x in tekst:
    if float(x[1])+(teepikkus*float(x[2]))<hindkoju:
        hindkoju=float(x[1])+(teepikkus*float(x[2]))
        odavaimtakso=x[0]
print("Kõige odavam taksofirma on",odavaimtakso+".")