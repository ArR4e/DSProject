try:
    fail=open("kinganumbrid.txt")
    rida=fail.read()
    kinganr = float(rida.strip())
    print(round(2/3*(kinganr- 2)))    
except:
    print("Vigane sisend.")
    
# Ei tule välja, lähen magama.