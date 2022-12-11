kaugus = int(input("Liini pikkus meetrites: "))
vahe = int(input("Vahe postide vahel meetrites: "))

if kaugus % vahe == 0:
    postid = kaugus // vahe + 1
else:
    postid = kaugus // vahe + 2

print(postid)