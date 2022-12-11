pikkus = int(input("Sisesta liini pikkus: "))
kaugus = int(input("Sisesta postide vaheline kaugus: "))

postid = 1

while pikkus / postid > kaugus:
    postid += 1
    
print(postid+1)
