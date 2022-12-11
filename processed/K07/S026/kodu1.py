järjend = ["Mati P", "Kati T", "Kadri T", "Toomas P", "Peep P"]
def poisse_ja_tüdrukuid(järjend):
    t = 0
    p = 0
    for rida in järjend:
        sugu = rida[-1]
        if sugu == "P":
            p += 1
        if sugu == "T":
            t += 1
    
    print(p, t)
        
poisse_ja_tüdrukuid(järjend)