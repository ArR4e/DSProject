sisend = input("Sisendfail: ")
väljund = input("Väljundfail: ")

with open(sisend, "r") as f:
    sisu = f.read()
    muudatused = sisu.count("Hello")
    uus_sisu = sisu.replace("Hello", "Tere")
with open(väljund, "w") as v:
    v.write(uus_sisu)
    
print(muudatused)