tulu = float(input("Sisesta aastatulu: "))

if tulu <= 6000:
    print(tulu)
    
if tulu <= 14400:
    print(6000)
    
if tulu >= 14400 and tulu <= 25200:
    print(round(6000-6000/10800*(tulu-14400),2))

if tulu > 25200:
    print(0)
    