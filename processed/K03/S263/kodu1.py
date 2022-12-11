
aastatulu = int(input("Sisesta aastatulu: "))

if 0 < aastatulu < 6000:
    print("Maksuvaba tulu on",aastatulu, "eurot")
elif 6000 <= aastatulu < 14400:
    print("Maksuvaba tulu on 6000 eurot aastas.")
elif 14400 <= aastatulu < 25200:
    maksuvabatulu =round(float(6000-6000/10800*(aastatulu - 14400)),2)
    print("Maksuvaba tulu on" ,maksuvabatulu, "eurot")
elif 25200 <= aastatulu:
    print("Maksuvaba tulu on 0 eurot")
    