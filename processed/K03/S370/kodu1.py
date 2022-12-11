
t=0
while not t> 0:
    try:
        t= int(input("Sisesta oma aastatulu: "))
        if t<0 or t==0:
          print("Tulu peab olema positiivne.")
    except:
        print("Sisesta number, mitte muud!")

if t <= 6000:
    mt=t
elif 6000<t<=14400:
     mt= 6000
elif 14400 < t <=25200:
   mt=6000-6000/10800*(t-14400)
else:
    mt=0

print("Maksuvaba tulu on", round(mt,2) , "eurot.")