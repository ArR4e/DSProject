nimi = input("Nimi: ")
loop = True

while loop:
    parool = input("Parool: ")
    parool2 = input("Parool uuesti: ")
    if parool != parool2:
        print("Parool ei kattu")
        continue
    if len(parool) < 8:
        print("Parool lühike")
        continue
    for i in parool:
        if i.isdigit():
            loop = False
            break
    else:
        print("Parool peab sisaldama nubreid")

fail = open("users.txt", "a")
loorap = ""
for i in parool:
    loorap = i + loorap

fail.write(nimi+":"+loorap)
fail.write("\n")
fail.close()