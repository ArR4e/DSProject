#a=liinipikkus
#b=maksimaalne postide vaheline kaugus
#+1=esimene post
from math import *
a=int(input("Liini pikkus"))
b=int(input("Kõrvutiasetsevate postide maksimaalkaugus m"))

print(ceil(a/b+1))

