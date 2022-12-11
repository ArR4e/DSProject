e = input("Eesnimi: ")
p = input("Perenimi: ")
kn = e.lower() + "." + p.lower()
if "õ" in kn:
    kn = kn.replace("õ", "o")
if "ö" in kn:
    kn = kn.replace("ö", "o")
if "ä" in kn:
    kn = kn.replace("ä", "a")
if "ü" in kn:
    kn = kn.replace("ü", "u")
print(kn)