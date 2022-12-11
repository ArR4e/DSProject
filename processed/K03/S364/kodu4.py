f = open("kinganumbrid.txt", encoding="UTF-8")
jopka = f.read().strip().split("\n")
if jopka == [""]:
    print("")
else :
    for i in jopka :
        try:
            arv = float(i)
            arv = 2/3 *(arv -2)
            print(round(arv))
        except :
            print("Vigane sisend")

