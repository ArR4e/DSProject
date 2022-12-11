pikkus=int(input("Sisestage liini pikkust (meetrites):"))
makskaugus=int(input("Sisestage postide maksimaalkaugust (meetrites):"))
post=pikkus//makskaugus
if pikkus%makskaugus>0:
    post +=1

print("Postide number on",post)