f = open("kinganumbrid.txt")
while True:
    kinganumber = f.readline()
    if kinganumber == "":
        break
    try:
        kinganumber2 = float(kinganumber.strip())
        pikkus =  2/3 * (kinganumber2 - 2)
        print (round(pikkus))
    except:
        print ("Vigane sisend")
f.close()