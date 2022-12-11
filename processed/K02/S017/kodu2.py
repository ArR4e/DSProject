import math
print("Täna ehitame sirgjoonelist elektriliini.")
print("Sirgjoonelise elektriliini ehitamisel paigutatakse" "\n" "kõrvutiasetsevad postid võrdsete kaugustega," "\n" "mis ei ületa etteantud maksimaalkaugust." "\n" "Liin algab ja lõpeb postiga.")
pikkus = int(input("Palun sisesta liini pikkus: "))
kaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus: "))

jagatis = pikkus / kaugus
    
x = math.ceil(jagatis) + 1

print("Liini ehitamiseks on minimaalselt vaja", x, "posti")
