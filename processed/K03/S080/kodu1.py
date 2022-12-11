a=float(input("Sisesta aastatulu (positiivne arv): "))
if a<6000:
    print("Maksuvaba tulu on",round(a,2),"eurot.")
elif a>=6000 and a<14400:
    print("Maksuvaba tulu on",6000,"eurot.")
elif a>=14400 and a<25200:
    print("Maksuvaba tulu on",round(6000-6000/10800*(a-14400),2),"eurot.")
else:
    print("Maksuvaba tulu on",0,"eurot.")