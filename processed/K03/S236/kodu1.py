#Maksuvaba tulu

aastatulu = float(input("Sisesta aastatulu: "))
valem = 6000 - 6000 / 10800 * (aastatulu - 14400)

if aastatulu < 6000:
    print("Maksuvaba tulu on ")
    print(round((aastatulu), 2))

elif 6000 <= aastatulu and aastatulu < 14400:
    print("Maksuvaba tulu on ")
    print(int(6000))

elif 14400 <= aastatulu < 25200:
    print("Maksuvaba tulu on ")
    print(round((valem), 2))

elif 25200 <= aastatulu:
    print("Maksuvaba tulu on ")
    print(0)
else:
    print("Kuna ei ole aastatulu, ei ole ka maksuvaba tulu")
    
