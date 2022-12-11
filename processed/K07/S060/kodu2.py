f=open("taksohinnad.txt","r")
def taksohind():
    kaugus=float(input("Sisesta tee pikkus kilomeetrites: "))
    odavaimhind=10000
    
    firma=0
    for rida in f:
        li=list(rida.split(","))
        kilomeetrit=li[2].rstrip()
        if (float(li[1])+kaugus*(float(kilomeetrit)))<odavaimhind:
            odavaimhind=(float(li[1])+kaugus*(float(kilomeetrit)))
            firma=li[0]
    print("Kõige odavam on "+firma)
taksohind()
f.close()

            