from math import*
pikkus=input(("sisesta soovitud liini pikkus meetrites: "))
vahe=input("sisesta soovitud postide vahe meetrites: ")
p=int(pikkus)
v=int(vahe)

arv=(p/v+1)
print((str(ceil(arv)) + " posti on vähemalt vaja liini rajamiseks" ))
