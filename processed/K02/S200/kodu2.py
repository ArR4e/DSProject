liini_pikkus = int(input("Sisestage liini pikkus meetrites: "))
maksimaalkaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites: "))

import math

postide_arv = liini_pikkus/maksimaalkaugus + 1
print(math.ceil(postide_arv))
