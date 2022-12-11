a = open(input("Sisesta faili nimi:")) #https://www.w3schools.com/python/python_file_open.asp
b = open(input("sisesta teise faili nimi:"), "a")
A = a.read()
c = A
B = A
if "Hello" in B:
    B = B.replace("Hello","Tere") #https://www.kite.com/python/answers/how-to-replace-characters-in-a-string-in-python
    b.write(B)
    print("Tehti " + str(c.count("Hello")) + " muudatust.")
else:
    print("Tehti 0 muudatust.")
a.close()
b.close()