aastatulu=float(input("Sisesta aastatulu: "))
#if aastatulu <= 0:
    #print ("Aastatulu ei tohi olla negatiivne.")
if aastatulu > 0 and aastatulu < 6000:
    maksuvaba=aastatulu
elif aastatulu >= 6000 and aastatulu < 14400:
    maksuvaba = 6000    
elif aastatulu >= 14400 and aastatulu < 25200:
    maksuvaba = round(6000 - 6000 / 10800 * (aastatulu - 14400), 2)
elif aastatulu >= 25200:
    maksuvaba = 0
print("Maksuvaba tulu on", maksuvaba,"eurot.")
