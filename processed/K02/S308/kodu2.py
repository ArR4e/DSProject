import math
kaugus=float(input("Palun sisesta liini pikkus(täisarv meetrites):"))
vahe=float(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugust(täisarv meetrites):"))

postid= kaugus / vahe +1
   
print(math.ceil(postid))