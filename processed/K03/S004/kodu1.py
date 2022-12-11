income = float(input("Sisesta aastatulu: "))
if income <= 6000:
    print("Maksuvaba tulu on",round(income,2),"eurot")
elif income > 6000 and income <= 14400:
     print("Maksuvaba tulu on","6000","eurot")
elif income > 14400 and income <= 25200:
     print("Maksuvaba tulu on",round(6000-6000/10800*(income-14400),2),"eurot")
elif income > 25200:
     print("Maksuvaba tulu on","0","eurot")