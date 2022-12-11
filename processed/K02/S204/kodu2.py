import math
from math import floor



a = int(input("Palun sisesta liini pikkus meetrites: "))
b = int(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
c= float(a/b)


if int(c):
 print("Minimaalselt on poste vaja:", math.ceil(c+1))
else:
  print("Error")

   
           

          
