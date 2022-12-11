fail = open("taksohinnad.txt", encoding = "UTF-8")

a = float(input("Sisesta tee pikkus kilomeetrites: "))

while True:
    
    b = fail.readline().strip()
    c = fail.readline().strip()
    d = fail.readline().strip()
    
   
    break
x = b.split(",")    
y = c.split(",")

z = d.split(",")
    
hind1 = float(x[1])+a*float(x[2])
hind2 = float(y[1])+a*float(y[2])
hind3 = float(z[1])+a*float(z[2])

e = min([hind1, hind2, hind3])


if e == hind1:
    print("Kõige odavam on Maksitaksi.")
    
if e == hind2:
    print("Kõige odavam on Sõps veab.")
    
if e == hind3:
    print("Kõige odavam on Waldo takso.")