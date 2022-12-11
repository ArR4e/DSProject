a=int(input("""Sisesta liini pikkus (täisarvuna meetrites): """))
b=int(input("""Sisesta kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): """))
c=(a//b)

if b/a>=1:
    c=2
elif a//b==0:
    c=c+3
elif b/a==0.5:
    c=a/b+1
else:
    c=c+2


print("Liini ehitamiseks on minimaalselt vaja",c,"posti")
