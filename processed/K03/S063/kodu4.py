f = open("kinganumbrid.txt")
while True:
    number = f.readline().strip()
    if number == "":
        break
    else:
        try:
          print(round(2/3*(int(number)-2)))
        except:
            print("Vigane sisend")

f.close()