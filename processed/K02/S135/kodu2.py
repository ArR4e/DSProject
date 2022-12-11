from math import *
liin = int(input("sisestage liini pikkus: "))
maxPostideVahe = int(input("sisestage postide vaheline maksimaalne kaugus: "))

postideArv = ceil(liin / maxPostideVahe) + 1

print("Liini ehitamiseks on minimaalselt vaja", postideArv)