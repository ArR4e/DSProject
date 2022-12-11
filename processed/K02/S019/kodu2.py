liin = int (input("Palun sisesta elektriliini pikkus täisarvuna meetrites: "))
post = int (input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites: "))
post.__floor__()

if liin % post ==0:
    arv = int(liin/post+1)
else:
    arv = int(liin/post+2)
    
(arv).__ceil__()
if arv <= 1:
    print ("2")
else:
    print(arv)