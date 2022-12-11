nimi = input("kasutajanimi: ")
parool1 = input("parool: ")
parool2 = input("parool: ")
if parool1 == parool2 and len(parool1)>= 8 and nimi.isalnum() :
    tagurpidi_parool = (parool1)[::-1]
    f = open("users.txt", "w")
    f.write(nimi)
    f.write(":")
    f.write(str(tagurpidi_parool))
    f.close()    
else:
    print("Viga. Proovige uuesti.")
    
    