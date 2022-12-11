pikkus = int(input("Sisesta liini pikkus täisarvuna: "))
kaugus = int(input("Sisesta 2 posti kaugus täisarvuna: "))

if kaugus > pikkus:
    print("Error, pikkus on liiga lühike!")
    exit()

else:
    postid = int(1 + (pikkus / kaugus))
    print("Elektriliini jaoks on vaja " + str(postid) + " posti.")
