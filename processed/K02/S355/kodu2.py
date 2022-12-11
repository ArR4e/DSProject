import math
m = input("Sisesta elektriliini pikkus meetrites:")
m = int(m)
maxKaugus = 1000
maxArv = 100
if (m > maxKaugus):
    print("See elektriliin on liiga pikk, proovi natuke vähem")
elif (m < 0):
    print("Negatiivse kaugusega on natuke raske opereerida, proovi uuesti.")
else:
    n = input("Sisesta elektripostide maksimaalne kaugus meetrites:")
    n = int(n)
    
    if (n > maxArv):
        print("Oioi, liiga palju poste - proovi natuke vähem")
    elif(n == 0):
        print("Kas sa tahad, et kõik postid oleksid üksteise sees? Proovi uuesti")
    elif (n < 0):
        print("Negatiivse kaugusega on natuke raske opereerida, proovi uuesti.")
    else:
       print (str(math.ceil(m/n) + 1) + " " + "meetrit")


