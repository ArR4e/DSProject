import math
kaugus = int(input ("Sisesta elektriliini pikkus meetrites: "))
postid = int(input ("Sisesta postide vaheline kaugus meetrites: "))
arv_võrdub=((kaugus/postid)+1)
number=math.ceil(arv_võrdub)
arv=max(2,number)
print(str(arv) + " posti")