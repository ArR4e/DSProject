kinganr=open("kinganumbrid.txt")

for rida in kinganr:
    try:
        arv=float(rida.strip("\n"))
        print(round(2/3*(arv-2)))
    except:
        print("Vigane sisend")

kinganr.close()