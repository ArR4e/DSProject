LähteFail = "kinganumbrid.txt"

f = open(LähteFail)

while True:
    rida = f.readline()
    #Kontrollin kas fail on tühi
    if rida == "" or rida == ('\n'): 
        break
    #Kontrollin kas tegemist on jamaga
    try:
        rida = float(rida)
    except:
        print("Vigane sisend")
        continue
    
    
    #teisendame numbri pikkuseks ja väljastame suuruse
    pikkus = 2/3 * (rida - 2)
    print(round(pikkus))
    
