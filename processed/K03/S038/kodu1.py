at=float(input("Sisestage aastatulu:"))
if 0 < at <= 6000:
    mv=at
elif 6000 < at <= 14400:
    mv=6000
elif 14400 < at <= 25200:
    mv= 6000-(6000/10800)*(at-14400)
else:
    mv=0
print (round(mv,2))
    