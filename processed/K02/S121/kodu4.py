en_file = input("Lähtefaili nimi: ")
est_file = input("Sihtfaili nimi: ")

text = ""
with open(en_file, "r") as file:
    for line in file:
        text += line
text_2 = text.replace("Hello", "Tere")
count = text.count("Hello")

print("Tehti " + str(count) + " asendamist")

with open(est_file, "w") as file_2:
    file_2.write(text_2)

file.close()
file_2.close()