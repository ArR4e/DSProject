tulu=float(input("Sisesta oma aastatulu eurodes: "))
i=0
if tulu <= 6000:
    vaba=tulu
elif tulu <=14400:
    vaba=6000
elif tulu <= 25200:
    vaba=6000-6000/10800*(tulu - 14400)
else:
    vaba=0
print("Maksuvaba tulu on",round(vaba,2),"€")
