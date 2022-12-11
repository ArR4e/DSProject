arv = int(input("Palun sisestage naturaalarv: "))
i = 1
a = 0
b = 0
while i <= arv:
   a = i**2 + a
   b = b + i
   i += 1
   
print("Summade erinevus on: "+str(b**2-a))