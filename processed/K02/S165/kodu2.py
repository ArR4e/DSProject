import math

LiiniPikkus = int(input("Palun sisestage kogu elektriliini pikkus "))
PostideKaugus = int(input("Palun sisestage elektriliini postide vaheline kaugus "))
PostideArv = math.ceil((LiiniPikkus  / PostideKaugus) + 1)

print("Minimaalne postide arv on", PostideArv)