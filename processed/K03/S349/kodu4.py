readFileName = open(input("Palun sisestage faili nimi: "))

while(readFileName.hasNextLine):
    try:
        jalalaba_pikkus_sentimeetrites = readFileName.readline()
        kinganumber_EU = readFileName.readline()
        jalalaba = 2 / 3 * (jalalaba_pikkus_sentimeetrites - 2)
        jalalaba_ümardatuna = round(str(jalalaba))
        print(jalalaba_pikkus_sentimeetrites)
        print(kinganumber_EU)
        print(jalalaba_ümardatuna)
    except:
        print("Vigane sisend")
        
readFileName.close()