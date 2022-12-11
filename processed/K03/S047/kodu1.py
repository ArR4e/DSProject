tulu=float(input("Sisesta siia, oma ülisalajane aasta palk: "))

if tulu>25200 :
    print("Maksuvaba tulu on 0 eurot")
elif 14400<tulu<=25200 :
    print("Maksuvaba tulu on", round(6000-6000/10800*(tulu-14400),2),"eurot")
elif 6000<tulu<=14400 :
    print("Maksuvaba tulu on 6000 eurot")
elif 0<=tulu<=6000 :
    print("Maksuvaba tulu on", tulu,"eurot")
else:
    print("Sisestasite midagi valesti")