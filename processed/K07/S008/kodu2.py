fail = open("taksohinnad.txt", encoding="UTF-8")

s = float(input("Sisesta sõidetav teepikkus: "))
maksilisti = []
sõbralisti = []
waldolisti = []
for rida in fail:
    
    #rida1 = fail.readline().strip()
    maksilisti = (rida).strip().split(",")
    
    
    rida2 = fail.readline().strip()
    sõbralisti = (rida2).split(",")
    
    
    rida3 = fail.readline().strip()
    waldolisti = (rida3).split(",")



hind1 = (float(maksilisti[1]) + float(maksilisti[2])* s)
hind2 = (float(sõbralisti[1]) + float(sõbralisti[2])* s)
hind3 = (float(waldolisti[1]) + float(waldolisti[2])* s)

if hind1 < hind2 and hind1 < hind3:
    print ("Maksitakso oleks kõige odavam")
    
elif hind2 < hind1 and hind2 < hind3:
    print ("Sõbratakso on kõige odavam")
    
elif hind3 < hind1 and hind3 < hind2:
    print ("Waldo takso on kõige odavam")

#hinnad = []
#hinnad.append(hind1)
#hinnad.append(hind2)
#hinnad.append(hind3)

#print (min(hinnad))
#print (maksilisti)
#print (sõbralisti)
#print (waldolisti)