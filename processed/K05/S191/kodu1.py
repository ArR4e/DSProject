k_nimi=input("Sisestage kasutajanimi: ")
while True:
    pass1=input("Sisestage parool: ")
    pass2=input("Sisestage uuesti: ")
    if pass1 !=pass2:   #kontrollin ühtivust
        print("Paroolid ei ühti \n")
    elif len(pass1)<8:   #kontrollin pikkust
        print("Parool liiga lühike\n")
    elif any(i.isdigit() for i in pass1)==False:   #kontrollin, kas ükski parooli elementidest on number
        print("Parool peab sisaldama numbreid\n")
    else:    #kõik vajadused on täidetud ja tsüklist saab väljuda
        break
krypt=pass1 [::-1]    #parool pööratakse ümber
f=open("users.txt","a")    #fail avatakse "append" abil, ehk eksisteerivat faili täiendatakse, ei kirjutata üle
f.write(k_nimi+":"+krypt+"\n")    #failile kirjutatakse soovitud formaadis
f.close()