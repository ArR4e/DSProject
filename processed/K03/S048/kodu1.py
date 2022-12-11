tulu= int(input("Sisesatge oma aastatulu: "))
if tulu <0:
    print("sisestasite valesti, tulu ei saa olla negatiivne")

if tulu <= 6000 and tulu >= 0:
    print(tulu, " eur on maksuvaba tulu")
    
if tulu >6000 and tulu <= 14400:
    print("6000 eur on maksuvaba tulu")
 
if tulu >14400 and tulu <= 25200:
    print(round(6000-(6000/10800)*(tulu- 14400),2), " eur on maksuvaba tulu")
    
if tulu >25200:
    print("0 eur on maksuvaba tulu")
    