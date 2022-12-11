f = open("kinganumbrid.txt")
while True:
    sisu=f.readline()
    if sisu == (""):
        break
    try: 
        number = (float(sisu))
        print(round((2/3)*(number-2)))
    except:
        print("Vigane sisend")
f.close()