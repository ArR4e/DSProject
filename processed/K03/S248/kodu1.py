x=float(input("Sisesta aastatulu: "))

if x<=6000:
    y=x
elif x<=14400:
    y=6000
elif x<=25200:
    y=6000-6000/10800*(x-14400)
else:
    y=0
    
print("Maksuvaba tulu on " + str(round(y, 2)) + " eurot.")