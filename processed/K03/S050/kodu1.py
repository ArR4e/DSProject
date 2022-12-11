aastatulu=float(input("Sisesta enda aastatulu(€):"))

if aastatulu<=6000:
    mvt=aastatulu
elif 6000<aastatulu<=14400:
    mvt=6000
elif 14400<aastatulu<25200:
    mvt=6000-6000/10800 *(aastatulu-14400)
elif 25200<=aastatulu:
    mvt=0



print("Maksuvaba tulu on "+ str(round(mvt , 2))+" eurot.")
