fail=open("kinganumbrid.txt", "rt")
for kinganumber in fail:
    try:
        pikkus=2/3*(float(kinganumber.strip())-2)
        print (round(pikkus))
    except:
        print ("Vigane sisend.")
fail.close()