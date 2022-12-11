from pykkar import *
create_world("""
#########
#       #
#       #
#   <   #
#       #
#       #
#########
""")

while not is_wall():
    step()
if is_wall() == False:
    paint()
elif is_wall() == True:
    right()

while not is_wall():
    step()
while is_wall() == True:
    right()
if is_wall() == False:
    paint()
elif is_wall() == True:
    right()
    if is_wall() == False:
        paint()
    
while not is_wall():
    step()
if is_wall() == False:
    paint()
elif is_wall() == True:
    right()
    if is_wall() == False:
        paint()
        
while not is_wall():
    step()
if is_wall() == False:
    paint()
elif is_wall() == True:
    right()
    if is_wall() == False:
        paint()

while not is_wall():
    step()
if is_wall() == False:
    paint()
elif is_wall() == True:
    right()
    if is_wall() == False:
        paint()
