fail = open("kinganumbrid.txt","r")
tekst = fail.readlines()
fail.close()
for i in tekst:
    try:
        print(round(2/3*(float(i)-2)))
    except:
        print("Vigane sisend")