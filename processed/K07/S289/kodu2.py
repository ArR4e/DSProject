f = open("taksohinnad.txt", encoding="UTF-8")
a = float(input("Sisesta kilomeetrite arv: "))
odav_hind = 0
hind = 0
for rida in f:
    rida = rida.strip()
    järjend = rida.split(",")
    nimed = järjend[0]
    sisseistumine = float(järjend[1])
    km_hind = float(järjend[2])
    hind = sisseistumine + a * km_hind
    if hind < odav_hind or odav_hind == 0:
        odav_hind = hind
        odavaim = nimed

print("Kõige odavam takso on " + odavaim + ".")
    
    


    
    
    
    
    




    


















    
    