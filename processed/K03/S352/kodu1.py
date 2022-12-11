aastatulu=float(input("Sisestage oma aastatulu "))
mvt=0
if 6000<aastatulu<=14400:
    mvt=6000
elif 14400<aastatulu<=25200:
    mvt=6000-6000/10800*(aastatulu-14400)
elif aastatulu>25200:
    mvt=0
else:
    mvt=aastatulu

print("Maksuvaba tulu on ", round(mvt,2), "eurot.")