fail = open("kinganumbrid.txt", "r")
for rida in fail:
    try:
       jalalaba_pikkus= 2/3 * (float(rida) - 2)
       print(round(jalalaba_pikkus))
    except:
        print("Vigane sisend")
    
    
fail.close()

