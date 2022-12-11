f1 = input("Sisestage lähtefail: ")
f2 = input("Sisestage sihtfail: ")

file1 = open(f1, encoding = "UTF-8")
file2 = open(f2, "w", encoding = "UTF-8")

file1_contents = file1.read()
file1.close()

i = file1_contents.count("Hello")
file2_contents = file1_contents.replace("Hello", "Tere")
file2.write(file2_contents)

file2.close()

print(i)