lähtefaili_nimi = input("Sisesta lähtefaili nimi: ")
sihtfaili_nimi = input("Sisesta sihtfaili nimi: ")

f = open(lähtefaili_nimi)
filedata = f.read()

hello_count = filedata.count("Hello")

new_file = filedata.replace("Hello", "Tere")

f.close()

f_new = open(sihtfaili_nimi, "w")
f_new.write(new_file)
f_new.close()


print(hello_count)
