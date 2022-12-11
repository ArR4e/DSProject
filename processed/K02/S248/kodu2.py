x=int(input("Sisesta liini pikkus täisarvuna meetrites: "))
y=int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites: "))

if x/y>1:
    if x%y>0:
        print(str(int(x/y+2)))
    else:
        print(str(int(x/y+1)))
else:
    print("2")