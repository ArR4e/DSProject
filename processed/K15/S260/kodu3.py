from datetime import *

def bussid(plaan):
        bussid = []
        valikud = []
        fail = open(plaan,"r")
        for rida in fail:
            bussid.append(((((datetime.strptime(rida[6:11],"%H:%M") - datetime.strptime(rida[:5],"%H:%M")).total_seconds()/3600)),rida.strip()))
        bussid.sort()
        for i in range(len(bussid)):
            if bussid[i][0]*float(bussid[i][1][12:]) <= bussid[0][0]*float(bussid[0][1][12:]) + 3:
                valikud.append((bussid[i][1][:5],bussid[i]))
        valikud.sort()
        print("Kaaluge järgnevaid busse:")
        for buss in valikud:
            print(buss[1][1])
       
plaan = input("Sisestage failinimi: ")
#plaan = "sõiduplaan.txt"
bussid(plaan)
