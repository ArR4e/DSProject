pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
fail = open("taksohinnad.txt", "r", encoding="UTF-8")
rida1 = []
rida2 = []
rida3 = []
if pikkus == 0:
    print()
else:
    r1 = fail.readline().strip().split(",")
    r2 = fail.readline().strip().split(",")
    r3 = fail.readline().strip().split(",")
    s1 = str(r1[0])
    s2 = str(r2[0])
    s3 = str(r3[0])
    km1 = float(r1[2])
    km2 = float(r2[2])
    km3 = float(r3[2])
    sh1 = float(r1[1])
    sh2 = float(r2[1])
    sh3 = float(r3[1])
    hind1 = sh1 + km1*pikkus
    rida1 += [hind1]
    hind2 = sh2 + km2*pikkus
    rida2 += [hind2]
    hind3 = sh3 + km3*pikkus
    rida3 += [hind3]
    if rida2 >= rida1 and rida1 <= rida3:
        print("Kõige odavam on ", s1, ".", sep="")
    elif rida1 >= rida2 and rida2 <= rida3:
        print("Kõige odavam on ", s2, ".", sep="")
    else:
        print("Kõige odavam on ", s3, ".", sep="")
        
