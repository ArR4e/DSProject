tulu = float(input("Sisesta siia oma aasta tulu : "))

if tulu <= 6000:
    maksu_vaba = tulu
elif tulu > 6000 and tulu <= 14400 :
    maksu_vaba = 6000
elif tulu > 14400 and tulu <=25200:
    maksu_vaba = 6000-(6000/10800*(tulu-14400))
elif tulu > 25200:
    maksu_vaba = 0

print("Maksuvaba tulu on " + str(round(maksu_vaba, 2)))