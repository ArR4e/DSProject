pikkus = int(input("Sisestage elektriliini pikkus: "))
kaugus = int(input("Sisestage elektriliini postide kaugus üksteisest: "))
post = 1
while pikkus > 0:
    post += 1
    pikkus -= kaugus
print(post)