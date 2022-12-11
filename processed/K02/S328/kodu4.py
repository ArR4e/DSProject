file = input("Lähtefaili nimi: ")
file2 = input("Sihtfaili nimi: ")

f = open(file, "r")
text = ""
for i in f:
    text += i
text2 = text.replace("Hello", "Tere")
count = text.count("Hello")
print("Tehti " + str(count) + " asendamist.")

new_file = open(file2, "w")
new_file.write(text2)

f.close()
new_file.close()
     