f = open("kinganumbrid.txt", "r")
i = 0
jalanr = ""
labapikkus = 0
while i < 4:
    i = i + 1
    jalanr = f.readline()
    jalanr = jalanr.strip('\n')
    try: 
        float(jalanr)
        jalanr = float(jalanr)
        labapikk = (2/3)*(jalanr - 2)
        labapikk = round(labapikk)
        print(labapikk,"\n")
    except ValueError:
        print("Vigane sisend","\n")
        
        
f.close()