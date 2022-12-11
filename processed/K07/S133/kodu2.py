a=open("taksohinnad.txt", encoding="utf8")
tee_pikkud=float(input("palun sisestage tee pikkus: "))
sõit2=100000000000
sõiduvahend2=""
for rida in a:
    rida1 = rida.split(",")
    
    sõiduvahend1=rida1[0]
    sõiduvahend1_algus=rida1[1]
    sõiduvahend1_kilomeeter=rida1[2].strip()
    sõit1=float(sõiduvahend1_algus)+float(tee_pikkud)*float(sõiduvahend1_kilomeeter)
    if sõit1 < sõit2 :
        sõit2=sõit1
        sõiduvahend2=sõiduvahend1
    elif sõit2 < sõit1:
        continue
print(" Kõige odavam on " + str(sõiduvahend2)+".")
a.close()