# y - liinipikkus
# z - postide max kaugus
# x - postide arv
# a - võrdne kaugus 

y = int(input("Sisesta täisarvuline liini pikkus: "))
z = int(input("Sisesta täisarvuline postide maksimaalne kaugus: "))

if y/z==2:
    x=3
elif y>z:
    x = int(y/z) + 1
    a = y/x
    x = int(y/a) + 1
else:
    x=2

print(x)
