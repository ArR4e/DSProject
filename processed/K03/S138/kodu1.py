x = int(input("Sisestage aastatulu:"))
if x > 25200:
    y = 0
elif x > 14400:
    y = 6000-6000/10800*(x-14400)
    y = round(y,2)
else:
    y = 6000
print("Maksuvaba tulu on "+str(y)+" eurot.")
