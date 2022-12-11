km = float(input("Km: "))

fail = open("taksohinnad.txt","r",encoding="utf-8")
tekst = fail.readlines()
fail.close()
if tekst != []:
    a = float(tekst[0].strip().split(",")[1]) + float(tekst[0].strip().split(",")[2])*km
    c = tekst[0].strip().split(",")[0]
    for i in tekst:
        b = float(i.strip().split(",")[1]) + float(i.strip().split(",")[2])*km
        if b < a:
            a = b
            c = i.strip().split(",")[0]
    
    print("Odavaim on:",c)
else:
    print("Peab jala minema")