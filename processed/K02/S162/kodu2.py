import math
a=int(input("sisesta elektriliini pikkus: "))
b=int(input("sisesta postide max vahekaugus: "))
c=int(math.ceil(a/b+1))
print("sul on vaja "+str(c)+" posti")