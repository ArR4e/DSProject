aastatulu = float(input("Sisesta aasta tulu: "))
if aastatulu < 6000:
    vastus = aastatulu
    print("Maksuvaba tulu on "+str(vastus)+" eurot.")
elif aastatulu >= 6000 and aastatulu <= 14400:
    vastus = 6000
    print("Maksuvaba tulu on "+str(vastus)+" eurot.")
elif aastatulu >= 14400 and aastatulu <= 25200:
    vastus = round(6000-6000/10800*(aastatulu-14400),2)
    print("Maksuvaba tulu on "+str(vastus)+" eurot.")
elif aastatulu > 25200:
    vastus = 0
    print("Maksuvaba tulu on "+str(vastus)+" eurot.")
