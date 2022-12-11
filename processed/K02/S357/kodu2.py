from math import ceil

a = int(input("Liini pikkus meetrites "))
b = int(input("Postide maksimaalkaugus üksteisest meetrites "))
x = int(a/b +1)

if x >= 2:
    print ("Minimaalne vajaminev postide arv on", ceil(x))
else:
    print ("Minimaalne vajaminev postide arv on", 2)