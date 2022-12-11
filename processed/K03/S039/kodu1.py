aastatulu=float(input("Sisesta oma aastatulu: "))
if aastatulu<6000:
    tulu=aastatulu
elif aastatulu<14400:
    tulu=6000
elif aastatulu<25200:
    tulu=6000-6000/10800*(aastatulu-14400)
else:
    tulu=0
print("Maksuvaba tulu on "+ str(round(tulu,2))+" eurot aastas.")