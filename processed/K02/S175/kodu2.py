liini_pikkus = int(input("Sisesta liini pikkus ja vajuta ENTER: "))
postide_maksimaalkaugus = int(input("Sisesta postide maksimaalne kaugus ja vajuta ENTER: "))

if liini_pikkus == postide_maksimaalkaugus:
      print("Liini ehitamiseks on vaja minimaalselt ", int(liini_pikkus / postide_maksimaalkaugus + 1), "posti ")
else:
    if liini_pikkus == 2 * postide_maksimaalkaugus:
        print("Liini ehitamiseks on vaja minimaalselt ", int(liini_pikkus / postide_maksimaalkaugus + 1), "posti")
    else:
        print("Liini ehitamiseks on vaja minimaalselt ", int(liini_pikkus / postide_maksimaalkaugus + 2), "posti ")


        
                


