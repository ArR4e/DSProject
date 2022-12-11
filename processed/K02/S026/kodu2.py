a = float(input("Palun sisesta liini piikus (täisarvuna meetrites): "))
b = float(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))

import math
print("Posti vaja liini ehitamiseks:", math.ceil (a / b))
