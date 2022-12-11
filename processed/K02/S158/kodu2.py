a = input("Sisesta elektriliini pikkus: ")
b = input("Sisesta postide kaugus: ")

c = int(a) / int(b)
e = int(a) % int(b)
if int(e) == 0:
    d = int(c) + 1
else:
    d = int(c) + 2
    if int(a) < int(b):
        d = 2
 
x = ("Liinide ehitamiseks on vaja vähemalt " + str(d) + " posti.")
print(x)