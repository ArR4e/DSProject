liin_pikkus=int(input("Sisestage liini pikkus täisarvuna meetrites: "))
postid_kaugus=int(input("Sisestage postide maximaalne kaugus täisarvuna meetrites:"))

jääk = liin_pikkus%postid_kaugus
if jääk>0:
    print(int(liin_pikkus) // int(postid_kaugus) + 2, "posti tuleb ehitada.")
else:
    print(int(liin_pikkus) // int(postid_kaugus) + 1, "posti tuleb ehitada.")
    #Selle ül tekst jäi alguses segaseks, pärast automaatkontrolli sain alles aru 