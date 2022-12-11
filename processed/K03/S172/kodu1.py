tulu = float(input("Sisesta aastatulu: "))

if tulu <= 6000:
    vaba = round(tulu, 2)
elif tulu <= 14400:
    vaba = 6000
elif tulu <= 25200:
    vaba = 6000 - 6000/10800*(tulu - 14400)
    vaba = round(vaba, 2)
else:
    vaba = 0
    
print("Maksuvabatulu on", vaba, "eurot.")