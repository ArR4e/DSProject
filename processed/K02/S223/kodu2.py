def elektriliin(pikkus, vahe):
    if pikkus%vahe != 0:
        postid = pikkus//vahe + 2
    else:
        postid = pikkus/vahe + 1
    return postid
    
a = int(input("liini pikkus: "))
b = int(input("postide maksimaalkaugus: "))
print(elektriliin(a,b))