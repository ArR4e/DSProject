f = open('kinganumbrid.txt')

while True:
        nimi=f.readline().strip()
        if not nimi:
            break
        try:
            pikkus=2/3*(float(nimi)-2)
            print(round(pikkus))
        
        except:
            print("Vigane sisend")
            pass
            
f.close()

#ma isegi ei tea kuidas kood lõpuks tööle läks aga ma proovisin sadu variante läbi 