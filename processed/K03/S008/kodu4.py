fail = open ("kinganumbrid.txt") #faili nimi peab olema avades sõnena

for rida in fail: #rida on muutuja nagu i
    try:
        pikkus = 2/3 * (float(rida) - 2)
        print (round(pikkus))
    except: #errori korral tulebki siia
        print ("Vigane sisend")