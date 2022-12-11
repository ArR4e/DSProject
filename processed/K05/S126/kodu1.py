#andmete sisestamised
kasutaja_nimi = input("Palun sisestage kasutajanimi: ")

while True:
    parool1 = input("Palun sisestage uus parool: ")
    parool2 = input("Palun sisetage uus parool uuesti: ")
#funktsioon
    if parool1 != parool2:
        print("Paroolid on erinevad!")
        continue
    elif len(parool2) < 8:
        print("Parool on liiga lühike!")
        continue
    elif any(n.isnumeric() for n in parool2) == False:
        print("Parool ei sisalda numbreid!")
        continue
    elif any(a.isalpha() for a in parool2) == False:
        print("Parool ei sisalda tähti!!")
        continue
    else:
        stringlength = len(parool2)
        slicedstring = parool2[::-1]
        print(slicedstring)
        break
fail = open("users.txt", 'r')
fail.write("Kasutajanimi: " + a + "Parool: " + slicedstring)
fail.close()
   
          


    
        
    