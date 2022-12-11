x = int(input("Liini pikkus täisarvuna meetrites"))
y = int(input("Kõrvutiasetsevate postide maksimaalkaugus meetrites"))

import math
z = math.ceil(x/y)
print(z+1)