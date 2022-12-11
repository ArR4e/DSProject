a=float(input("Sisesta aasta tulu eurodes:"))
b=("Maksuvaba tulu on ") 
if 6001>a:
    print(b+str(a))
elif 6000<a<14401:
    print(b+str(6000))
elif 14400<a<25200:
    x=(round((6000-6000/10800*(a-14400)),2))
    print(b+str(x))
elif 25200<=a:
    print(b+str(0))
