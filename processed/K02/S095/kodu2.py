x=input("Sisesta elektriliini pikkus: ")
y=input("Sisesta postide vahemaa: ")

#if type(x)==int and type(y)==int:
#    print(x, y)
if x<y:
    print("Sisesta sobiv postide vahemaa")
else:
    z=int(x)//int(y)+1
    print("Sinu elektriliinile saab rajada ", z, " posti")