a=int(input("sisesta naturaalarv: "))
b=1
ruutude_summa=0
c=0
while b<=a:
    ruutude_summa += b**2
    c+=b
    b+=1
print("summa ruudu ja ruutude summa vahe on: " + str(c**2-ruutude_summa))
    
