f = open("kinganumbrid.txt", "r", encoding="UTF-8")

while True:
    kiriandmed= f.readline()
    if kiriandmed == "": #kui saab tühja sõne, siis lõpetab lugemise
        break
    try:
        arvandmed=float(kiriandmed) #enne pean tegema sõne arvuks
        jala_pikkus=(round(2/3 *(arvandmed -2)))
        print(jala_pikkus)
    except:
        print("Vigane sisend")
        
f.close()