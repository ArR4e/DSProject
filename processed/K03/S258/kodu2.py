from pykkar import *

x_width = int(input("Sisesta maailma laius "))
y_width = int(input("Sisesta maailma pikkus "))
print("Maailma koordinaadistikus on nullpuntkiks vasak ülemine ots, kust siis x telg jookseb paremale ja y telg alla! \n Palume seda tähele panna Pykkari algkoordinaatide otsustamisel!")
pykkar_pos_x = int(input("Sisesta pykkari alguspunkti x koordinaat (peab jääma vahemikku 1 - "+str(x_width)+") "))
pykkar_pos_y = int(input("Sisesta pykkari alguspunkti y koordinaat (peab jääma vahemikku 1 - "+str(y_width)+") "))
pykkar_suund= input("Sisestage palun pykkari suund (kas <, ^, > või v) ")
world=""
x=0
y=0
#antud ülesandes pole pykkar vaatamise suund oluline algpositsioonil, seega pole vahet, kas ta on "<" või ">" vms
while y!= y_width+2:
    while x!= x_width+2:
        if x==0 or x== x_width+1 or y==0 or y== y_width+1:
            world+="#"
        else:
            if x==pykkar_pos_x and y==pykkar_pos_y:
                world+=pykkar_suund
            else:
                world+=" "
        x+=1
    world+="\n"
    x=0
    y+=1
create_world(world)
corners = 0
while corners !=4:
    while not is_wall():
        step()
    right()
    right()
    right()
    if is_wall():
        paint()
        corners+=1
    right()
    right()
    continue
