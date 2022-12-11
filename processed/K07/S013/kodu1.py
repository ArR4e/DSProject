x=[]
def poisse_ja_tüdrukuid(x):
    tüdruk = 0
    poiss = 0
    for rida in x:
        uus_x =rida.split(" ")
        sugu = uus_x[-1]
        if sugu == "T":
            tüdruk += 1
        elif sugu == "P":
            poiss += 1
    return poiss, tüdruk

print(poisse_ja_tüdrukuid(x))