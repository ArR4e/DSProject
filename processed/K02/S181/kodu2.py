try:
    liini_pikkus = int(input("Sisestage liini pikkus meetrites: "))
    postide_kaugus = int(input("Sisestage postide omavaheline maksimaalne kaugus: "))
    postide_arv = 0
    if liini_pikkus % postide_kaugus != 0:
        postide_arv = liini_pikkus // postide_kaugus + 2
        print("Läheb vaja "+str(postide_arv)+" posti")
    elif liini_pikkus % postide_kaugus == 0:
        postide_arv = liini_pikkus // postide_kaugus + 1
        print("Läheb vaja "+str(postide_arv)+" posti")
    else:
        print("Tundmatu viga")
except ValueError:
    print("Sisestage täisarv!")
except:
    print("Tundmatu viga")