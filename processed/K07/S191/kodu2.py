km=float(input("Kui pikk maa on vaja sõita (km)? "))
f=open("taksohinnad.txt","r",encoding="UTF-8")
parim=km*1000
parimList=[0,1]
for line in f:
    strip=line.strip()
    lineList=strip.split(",")
    #print(lineList)
    hind=km*float(lineList[2])+float(lineList[1])
    #print(hind)
    if hind<parim:
        parim=hind
        parimList=lineList
print("Kõige odavam on",parimList[0])  