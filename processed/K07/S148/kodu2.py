x = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", encoding="UTF-8")

i = 1000000000
j = ""
for rida in f:
    a = rida.strip().split(",")
    
    b = float(a[1]) + float(a[2]) * x
    
    if b < i:
        i = b
        t = a[0]

print("Kõige odavam on " + t + ".")

f.close()