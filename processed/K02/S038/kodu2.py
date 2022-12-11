liin=int(input("Sisesta liini pikkus meetrites:"))
kaugus=int(input("Sisesta postide maksimaalkaugus meetrites:"))
postid=((liin//kaugus))
if liin%kaugus == 0:
    print (postid+1,"posti")
else:
    print (postid+2,"posti")
