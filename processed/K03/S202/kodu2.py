from pykkar import *

create_world("""
########
#      #
#      #
#   <  #
#      #
########
""")
#Uurib mis suunas on, sellest orienteerudes suundub alla
gd = get_direction()

if gd == "S":
    while not is_wall():
        step()
elif gd == "W":
    right()
    right()
    right()

elif gd == "N":
    right()
    right()
    
elif gd == "E":
    right()

gd=get_direction()

if gd == "S":
    while not is_wall():
        step()
#On jõudnud madailamasse punkti
right()

while not is_wall():
    step()
right()
#On jõudnud vasakusse alumisse nurka ja võtnud suuna N
#Läheb ja värvib nurgad üle
paint()              #Värvib vasaku alumise nurga
while not is_wall():
    step()
right()
paint()              #Värvib vasaku ülemise nurga

while not is_wall():
    step()
right()
paint()              #Värvib parema ülemise nurga

while not is_wall():
    step()
paint()              #Värvib parema alumise nurga

print("Nurgad värvitud")


