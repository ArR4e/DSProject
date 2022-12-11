fail = open("kinganumbrid.txt")


for rida in fail:
    try:
        kinganumber = float(rida.strip())
        jalalaba_pikkus = 2/3 * (kinganumber-2)
        ümardatud_pikkus = round(jalalaba_pikkus)
        print(ümardatud_pikkus)
    except:
        print("Vigane sisend")
    
fail.close()