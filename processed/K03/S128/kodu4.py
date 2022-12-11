fail = open("kinganumbrid.txt", encoding="UTF-8")    
for rida in fail:
    try:
        kinganumber = rida.strip()
        jalalaba_pikkus = round(2/3*(float(kinganumber)-2))
        print(jalalaba_pikkus)
    except:
        print("Vigane sisend")
fail.close()