at = float(input("Sisesta oma aastatulu: ")) #at tähendab aastatulu
if at <= 6000:
    print("Maksuvaba tulu on: " + str(at) + " eurot")

elif 6000 <= at <= 14400:
    print("Maksuvaba tulu on 6000 eurot")

elif 14400 < at <= 25200:
    print(round((6000 - ((6000 / 10800) * (at - 14400))), 2)) #Liigsed sulud
                                                              #enda mugavuseks
elif at > 25200:
    print("Maksuvaba tulu on 0 eurot, teenid üle keskmise palga")
    


