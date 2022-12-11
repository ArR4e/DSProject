from math import pi

def koogi_hind(kooginimi, mõõt):
    global hind
    if kooginimi=="Napoleoni kook":
        hind = ss
        print(f"koogi hind on {hind} eurot")
    elif kooginimi=="šokolaadikook":
        hind = s
        print(f"koogi hind on {hind} eurot")
    elif kooginimi=="ploomikook":
        hind = sss
        print(f"koogi hind on {hind} eurot")
    else:
        raise ("Sellist kooki andmebaasist ei leitud")
    return

while True: 
    
kooginimi = input("sisestage kooginimi: ")
mõõt = float(input("sisestage koogi mõõt sentimeetrites: "))
s = round((((mõõt**2)*pi)*0.06), 2)
ss = round(((mõõt**2)*0.1), 2 )
sss = round(((mõõt**2)*pi)*0.04, 2)
koogi_hind(kooginimi, mõõt)
  
  



