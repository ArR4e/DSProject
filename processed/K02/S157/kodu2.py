import math
#küsin liini pikkust
liin= int(input("Sisesta soovitud liini pikkus meetrites: "))
#küsin kõrvutiasetsevate postide maksimaalkaugust
kaugus= int(input("Sisesta soovitud kõrvutiasetsevate postide maksimaalkaugus meetrites: "))


post=liin/kaugus

vastus=math.ceil(post)

v1=vastus+1
print("ehitmiseks läheb vaja",v1,"posti.")


