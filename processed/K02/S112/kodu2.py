x=int(input("Sisesta liini pikkus täisarvuna meetrites:"))
y=int(input("Sisesta maksimaalne postidevaheline kaugus meetrites:"))
import math
print(round(math.ceil(x/y)+1))