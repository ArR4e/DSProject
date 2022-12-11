tulu = float(input("Sisesta aastatulu:"))
if tulu <= 6000:
    mvaba = tulu
else:
    if tulu <= 14400:
        mvaba = 6000
    else:
        if tulu <=25200:
            mvaba = 6000 - 6000/10800*(tulu-14400)
        else:
            mvaba=0
mvaba = round(mvaba,2)
print(mvaba)