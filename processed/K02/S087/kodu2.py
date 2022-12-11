a = float(input ("Liini pikkus meetrites: "))
b = float(input("Kõrvutiasetsevate postide kaugus: "))
if a < b:
    print (2)
elif a % b == 0:
    print (a // b + 1)
else:
    print (a // b + 2)