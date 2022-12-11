aastatulu = float(input("Sisesta aastatulu: "))
if (aastatulu < 0):
    print("Vale vastus, vali uus")
elif (aastatulu < 6000):
    print("Maksuvaba tulu suurus on: ", aastatulu)
elif (aastatulu >= 6000 and aastatulu < 14400):
    print("Maksuvaba tulu suurus on: ", 6000)
elif (aastatulu >= 14400 and aastatulu < 25200):
    print("Maksuvaba tulu suurus on: ", round(6000-6000/10000*(aastatulu - 14400), 2))
else:
    print("Maksuvaba tulu suurus on 0 eurot") 