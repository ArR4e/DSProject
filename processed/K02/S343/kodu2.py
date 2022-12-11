import math
liiniPikkus= int(input("Sisesta liini pikkus meetrites: "))
maxKaugus= int(input("Siseta maksimaalne postidevaheline kaugus meetrites: "))
    
postideArv = math.ceil(liiniPikkus / maxKaugus + 1)
if postideArv == 0:
    print("Maksimaalne postidevaheline pikkus ei saa olla suurem kui liini pikkus.")
elif postideArv == 1:
    postideArv += 1
    Print("Minimaalne postide arv on " + (str(postideArv)))
elif postideArv > 1:
    print("Minimaalne postide arv on " + (str(postideArv)))
   