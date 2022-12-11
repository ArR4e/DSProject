from math import ceil

pikkus = int(input("Sisesta siia liini pikkus meetrites ning vajuta Enter:"))
kaugus = int(input("Sisesta siia kõrvutiasetsevate postide maksimaalkaugus meetrites ning vajuta Enter:"))

vahe= (ceil( pikkus / kaugus + 1))
print (vahe)

