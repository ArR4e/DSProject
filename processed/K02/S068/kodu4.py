a = input("Lähtefaili nimi: ")
b = input("Sihtfaili nimi: ")
c = 0

f = open(b, "w")
file = open(a)
for rida in file:
    c = c + rida.count("Hello")
    f.write(rida.replace("Hello", "Tere"))
    
    
f.close()
file.close()
    

print("Tehti " + str(c) + " astendamist")
            
    