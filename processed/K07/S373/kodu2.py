a = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", "r")
odavam = 0
for rida in f.readlines():
  järjend = rida.rstrip().split(",")
  sõiduhind = float(järjend[1]) + (a * float(järjend[2]))
  if sõiduhind < odavam or odavam == 0:
      odavam = sõiduhind
      odavam_takso = järjend
f.close()
print("Kõige odavam on " + " hinnaga " + odavam_takso[0] + ".")