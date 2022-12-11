tee = float(input("Sisesta teekonna pikkus: "))
if tee == 0:
    print("")
else:
    fail = open("taksohinnad.txt",encoding="UTF-8")
    rida1 = fail.readline()
    rida2 = fail.readline()
    rida3 = fail.readline()
    rida4 = fail.readline()
    a = []
    b = []
    c = []
    d = []
    a = rida1.split(",")
    b = rida2.split(",")
    c = rida3.split(",")
    d = rida4.split(",")
    a1 = float(a[1])+float(a[2])*tee 
    a2 = float(b[1])+float(b[2])*tee
    a3 = float(c[1])+float(c[2])*tee
    a4 = float(d[1])+float(d[2])*tee
    if a1< a2 and a1<a3 and a1 < a4:
        ots = a[0]
    elif a2< a1 and a2<a3 and a2< a4:
        ots = b[0]
    elif a3< a1 and a3<a2 and a3 < a4:
        ots = c[0]
    elif a4< a1 and a4<a2 and a4 < a3: 
        ots = d[0]

    print("Kõige odavam on",ots+".")


