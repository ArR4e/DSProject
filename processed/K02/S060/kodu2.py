pikkus= int(input("Mis on liini pikkus:"))
postid= int(input("Postide maksimaalne kaugus:"))
arv = pikkus // postid +1
lisa = pikkus % postid
if lisa > 0:
    arv=arv+1
print(arv)