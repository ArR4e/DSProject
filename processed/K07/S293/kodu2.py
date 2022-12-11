km=float(input("Sisestage kilomeetrite arv: "))

f=open("taksohinnad.txt", encoding="UTF-8")
sisu=f.read()
if sisu!="":
    read=sisu.split("\n")
    takso1=read[0].split(",")
    takso2=read[1].split(",")
    takso3=read[2].split(",")
    
    takso1hind=km*float(takso1[2])+float(takso1[1])
    takso2hind=km*float(takso2[2])+float(takso2[1])
    takso3hind=km*float(takso3[2])+float(takso3[1])
    for i in range(1):
        if takso1hind<takso2hind and takso1hind<takso3hind:
            print("Kõige odavam on", takso1[0]+".")
            break
        if takso2hind<takso1hind and takso2hind<takso3hind:
            print("Kõige odavam on", takso2[0]+".")
            break
        if takso3hind<takso2hind and takso3hind<takso1hind:
            print("Kõige odavam on", takso3[0]+".")
            break
else:
    print("Takso info puudub")

