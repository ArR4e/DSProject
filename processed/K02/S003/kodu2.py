import math
a = int(input("palun sisesta liini pikkus meetrites: "))
b = int(input("palun sisesta kõrvutiasetsevate postide maksimaalkaugus meetrites: "))

postideArv = math.ceil((a/b) + 1)

print(postideArv)