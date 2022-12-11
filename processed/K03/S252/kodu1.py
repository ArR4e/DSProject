aastatulu = float(input("Sisesta aastatulu:"))
if aastatulu <= 6000:
    round (aastatulu, 2)
    print (aastatulu)
elif aastatulu >= 6000 and aastatulu <= 14400:
    print ("Maksuvaba tulu 6000 eurot aastas")
elif aastatulu >= 14400 and aastatulu <= 25200 :
    aastatulu2 = (6000 - (6000 / 10800) * (aastatulu - 14400))
    ymardatud = round (aastatulu2, 2)
    print (ymardatud)  
elif aastatulu > 25200:
    print ("Maksuvaba aasta tulu on 0 eurot")