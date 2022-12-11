kaugus = int(input("Sisesta postide vaheline kaugus meetrites: "))
pikkus = int(input("Sisesta elektriliini pikkus meetrites: "))
postid = pikkus / kaugus + 1
print("Elektriliini ehitamiseks on vaja minimaalselt", int(postid), " posti.")