fail = open('kinganumbrid.txt')

for rida in fail:
    try:
        kinganr = float(rida.strip())
        jalalaba_pikkus = round(2/3*(kinganr - 2))
        print(jalalaba_pikkus)
    except:
        print("Vigane sisend")
        
fail.close()