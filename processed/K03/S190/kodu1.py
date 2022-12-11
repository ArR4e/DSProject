aastatulu = float(input("Sisesta oma aastatulu: "))

if aastatulu <= 6000:
    print("Maksuvaba tulu on "+str(aastatulu)+" aastas.")

elif aastatulu >= 6000 and aastatulu <= 14400:
    print("Maksuvaba tulu on 6000 aastas.")
    
elif aastatulu >= 14400 and aastatulu <= 25200:
    print("Maksuvaba tulu on "+str(round(6000-6000/10800*(aastatulu-14400),2))+" aastas.")

elif aastatulu >= 25200:
    print("Maksuvaba tulu on 0 eurot.")