tulu=float(input("Sisesta aastatulu: "))
vaba=0
if tulu>25200:
    vaba=0
elif tulu>=14400 and tulu<=25200:
    vaba=6000-6000/10800*(tulu-14400)
elif tulu>=6000 and tulu<=14400:
    vaba=6000
else:
    vaba=tulu
print("Maksuvaba tulu on "+str(round(vaba,2))+" eurot.")