#jalalaba_pikkus = 2/3*(kinganumber-2)

f = open("kinganumbrid.txt")

#kinganumber = int(rida.strip())

while True:
    rida = f.readline()
    if rida == "" :
        break
    else:
        try:
            kinganumber = round((2/3 * (float(rida) - 2)))
            print(kinganumber)
        except:
            print("Vigane sisend")
            
            
f.close()

       
        
        
        
        




