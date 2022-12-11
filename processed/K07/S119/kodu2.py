pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
if pikkus > 0:
    fail = open("taksohinnad.txt", "r")
    uuedhinnad = []
    uuednimed = []
    for takso in fail:
        jarjend = takso.split(",")
        hind = float(jarjend[1]) + pikkus*float(jarjend[2])
        nimed = jarjend[0]
        uuedhinnad = uuedhinnad + [hind]
        uuednimed = uuednimed + [nimed]
    if uuedhinnad[0] < uuedhinnad[1] and uuedhinnad[0] < uuedhinnad[2]:
        print("Kõige odavam on " + uuednimed[0])
    if uuedhinnad[1] < uuedhinnad[0] and uuedhinnad[1] < uuedhinnad[2]:
        print("Kõige odavam on " + uuednimed[1])
    if uuedhinnad[2] < uuedhinnad[0] and uuedhinnad[2] < uuedhinnad[1]:
        print("Kõige odavam on " + uuednimed[2])

    fail.close()
        
else:
    print("Vale teade")
    





    
    
