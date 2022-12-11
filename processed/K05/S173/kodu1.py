import re

file = open("users.txt", "w") #https://www.guru99.com/reading-and-writing-files-in-python.html
nimi = input("Sisesta kasutajanimi:")
krüpt = ""
while True:
    parool1 = input("Sisesta parool:")
    parool2 = input("Sisesta parool uuesti:")
    if parool1 != parool2:
        continue
    if len(parool1)<8: #https://discuss.codecademy.com/t/python-how-to-count-number-of-letters-in-a-string/78055/2
        continue
    if re.search("[a-z]", parool1.lower()): #https://www.geeksforgeeks.org/python-program-check-validity-password/
        if re.search("[0-9]", parool1):
            break
for i in parool1:
    krüpt = i + krüpt
file.write(nimi + ":" + krüpt)
file.close()