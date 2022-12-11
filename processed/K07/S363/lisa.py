from turtle import *

f = open("värvid.txt")

värvid = []
sulgudega = []
a = 0

for i in f:
    rida = i.split(" ")
    
    for värv in rida:
        if "\n" in värv:
            värv = värv.strip("\n")
            
        if "{" in värv:
            värv = värv.strip("{")
            sulgudega.append(värv)
            a = 1
            
        elif a == 1:
            indeks = len(sulgudega) - 1
            
            if "}" in värv:
                värv = värv.strip("}")
                sulgudega[indeks] = sulgudega[indeks] + " " + värv
                a = 0
                
                värvid.append(sulgudega[indeks])
                
            else:
                sulgudega[indeks] = sulgudega[indeks] + " " + värv
                  
            
        elif a == 0 and värv != '' and "{" not in värv and "}" not in värv:
            värvid.append(värv)
            
print(sulgudega)
print(värvid)
kraad = 360/len(värvid)

speed(0)

for i in värvid:
    speed(0)
    pencolor(i)
    fillcolor(i)
    begin_fill()
    forward(600)
    left(90)
    circle(600,kraad)
    left(90)
    forward(600)
    end_fill()
    right(180)