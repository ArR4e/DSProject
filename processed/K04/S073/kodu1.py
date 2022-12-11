import math
prices = {
    "šokolaadikook": 0.06,
    "ploomikook": 0.04,
    "napoleoni kook": 0.1
}

def koogi_hind(name, r):
    name = name.lower()
    r = float(r)
    if name == "napoleoni kook":
        return round(prices[name]*r*r,2)
    if name in ["šokolaadikook", "ploomikook"]:
        return round(prices[name]*math.pi*r*r,2)
    else: raise

while True:
    cake = input("Sisesta kook: ")
    if not cake:
        break
    radius = input("Sisesta raadius: ")
    
    try:
        price = koogi_hind(cake.lower(),radius)
        print(price)
    
    except:
        print("Sellist kooki andmebaasist ei leitud")