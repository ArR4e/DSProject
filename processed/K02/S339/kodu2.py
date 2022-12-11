import math
a = int(input("Sisestage elektriliini pikkus meetrites: "))
b = int(input("Sisestage postide vaheline kaugus meetrites: "))
c = ((a/b)+1)
d = math.ceil(c)
e = max(2,d)
print(str(e) + " posti")