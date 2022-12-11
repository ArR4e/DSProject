liini_pikkus = float(input ("Sisesta liini pikkus (täisarvuna meetrites) "))
postide_maksimaalkaugus = float (input ("Sisesta kõrvutiasetsevate postide maksimaalkaugus üksteisest (täisarvuna meetrites "))
if liini_pikkus == postide_maksimaalkaugus:
    print (2)
if liini_pikkus == 2*postide_maksimaalkaugus:
    print (3)
else:
    print (int(liini_pikkus / postide_maksimaalkaugus + 2))

