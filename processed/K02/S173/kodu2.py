pikkus = int(input("Elektriliini pikkus meetrites:"))
max_vahe = int(input("Maksimaalne vahe kahe posti vahel:"))
if max_vahe < pikkus:
    postid = int(pikkus / max_vahe + 2)
    if pikkus / max_vahe ==2:
        postid = 3
    else:
        postid = int(pikkus / max_vahe + 2)
else:
    postid = 2
print("Liini jaoks on vaja", int(postid), "posti.")