f=open("taksohinnad.txt")
tee_pikkus=float(input("Kui kaugel kodu on?"))
odav=100000
nimi1="puudu"
while True:
    takso1=f.readline()
    if takso1=="":
    
       break
    else:
        takso1= takso1.split(",")
        nimi=takso1[0]
        sisse=takso1[1]
        kilomeeter=takso1[2].split("\n")
        hind=float(sisse)+float(kilomeeter[0])*tee_pikkus
        if hind<odav:
            odav=hind
            nimi1=nimi
        else:
            continue
print("Kõige odavam takso on "+nimi1+".")
