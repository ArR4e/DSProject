import math

pikkus = int(input("Elektriliini pikkus täisarvuna: "))
postide_kaugus = int(input("Kõrvutiasetsevate postide maksimaalkaugus täisarvuna: "))

tulemus = math.ceil(pikkus/postide_kaugus + 1)

if pikkus < postide_kaugus:
    print("Elektriliini pikkus peab olema suurem või võrdne postidevahelise kaugusega.")

elif pikkus == postide_kaugus:
    print("Elektriliini ehitamiseks on minimaalselt vaja 2 posti.")

else:
    print("Elektriliini ehitamiseks on minimaalselt vaja " + str(tulemus) + " posti.")