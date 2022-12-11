x = input("Lähtefaili nimi")
y = input("Sihtfaili nimi")

with open(x, "r", encoding="UTF-8") as fx:
    fxdata = fx.read()
    
z = fxdata.count("Hello")
fxdata = fxdata.replace("Hello", "Tere")

with open(y, "w", encoding="UTF-8") as fy:
    fy.write(fxdata)
    
fx.close()
fy.close()
print(z)