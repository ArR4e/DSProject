tulu=float(input("Sisesta aastatulu(mittenegatiivne arv): "))

if tulu<=6000:
    print("Maksuvaba tulu on sel juhul", str(round(tulu,2)), "eurot aastas.")
elif tulu>6000 and tulu<=14400:
    print("Maksuvaba tulu on sel juhul 6000 eurot aastas.")
elif tulu>14400 and tulu<=25200:
    print("Maksuvaba tulu on sel juhul", str(round(6000-6000/10800*(tulu-14400), 2)), "eurot aastas.")
else:
    print("Maksuvaba tulu on sel juhul 0 eurot aastas.")