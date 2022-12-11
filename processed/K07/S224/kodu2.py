

teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding = "UTF-8")

read = f.readlines()
minhind = 0
minnimi = ""

for taksonimi in read:
    taksonimi = taksonimi[0:-1]
    strvahe = taksonimi.split(",")
    hind = (teepikkus * float(strvahe[2])) + float(strvahe[1])
    if minnimi == "":
        minnimi = strvahe[0]
        minhind = hind
    
    elif hind < minhind:
        minhind = hind
        minnimi = strvahe[0]

print("Kõige odavam on", minnimi)
   
   

   