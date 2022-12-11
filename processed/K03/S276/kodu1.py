tulu=float(input("Sisesta aastatulu: "))
if tulu <= 6000:
    maksuv=tulu
elif tulu <= 14400:
    maksuv=6000
elif tulu <= 25200:
    maksuv=6000-6000/10800*(tulu-14400)
else:
    maksuv=0
print("Maksuvaba tulu on "+str(round(maksuv,2))+" eurot.")