fail = open("kinganumbrid.txt")

while True:
    try:
        for rida in fail:
            jalalaba_pikkus = round(2/3 * (float(rida) - 2))
            print(str(jalalaba_pikkus))
    except:
        print("Vigane sisend")
        
fail.close()

