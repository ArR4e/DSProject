from pykkar import*
'''import random
while True:
    try:
        laius = int(input("Sisesta maailma laius: "))
        kõrgus = int(input("Sisesta maailma kõrgus: "))
        if laius <= 2 or kõrgus <= 2:
            raise Exception
        break
    except:
        print("Mõlemad arvud peavad olema mittenegatiivsed naturaalarvud suuremad kui 2.")

suundade_variandid = ["^", ">", "v", "<"]
suund = random.choice(suundade_variandid)
x_telg = random.randint(2, laius - 1)
y_telg = random.randint(2, kõrgus - 1)
print(x_telg, y_telg)
a = laius - x_telg - 1


j = 1
maailm = open("maailm.txt", 'w')
while j <= kõrgus:
    if j == 1 or j == kõrgus:
        maailm.write("#" * laius + "\n")
    else:
        if j == y_telg:
            maailm.write("#" + (x_telg - 2) * " ")
            maailm.write(suund)
            maailm.write(a * " " + "#" + "\n")
        else:
            maailm.write("#" + (laius - 2) * " " + "#" + "\n")
    j = j + 1
maailm.close()

maailm = open("maailm.txt", 'r')
print(maailm.read())             ### See osa teeb faili nimega maailm.txt ning paigutab sinna Pykkari maailma koos
                                     kasutajalt saadud mõõtmetega ning juhusliku Pykkari suuna ja alguspositsiooniga.
                                     Seejärel prinditakse maailm ning soovi korral võib teda kasutada "create_world"
                                     käsuga ###'''

create_world("""
##########
#        #
#  <     #
#        #
#        #
#        #
#        #
#        #
#        #
##########
""")

while not is_wall():
    step()
right()
i = 0
while i < 4:
    while not is_wall():
        step()
    paint()
    right()
    i = i + 1
exitonclick()