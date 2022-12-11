liin_pikkus=a=input("Palun sisestage soovitud liini pikkus: ")
postide_maksimaalkaugus=b=input("Palun sisestage kõrvutiasetsevate postide maksimaalkaugus: ")
c=(int(a)/int(b)+1)
d=int(a)%int(b)
if d > 0:
    c=c+1

print("Teie elektriliini ehitamiseks on minimaalne postide arv: ", int(c))
