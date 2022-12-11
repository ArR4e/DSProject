a=int(input("sisesta liini pikkus: "))
b=int(input("sisesta postide vaheline max kaugus: "))
if a/b<1 or a//b<a/b:
    c=(a//b)+2 
else:
    c=a//b+1
print("minimaalne postide arv: " + str(c))
