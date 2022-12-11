from pykkar import *
create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")
a=get_direction()
b=0
if a=="N":
    while is_wall()==False:
        step()
    right()
    while is_wall()==False:
        step()
    paint()
    b+=1
if a==E and b==0:
    right()
    right()
    right()
    while is_wall()==False:
        step()
    right()
    while is_wall()==False:
        step()
    paint()
    b+=1
if a=="S" and b==0:
    right()
    right()
    while is_wall()==False:
        step()
    right()
    while is_wall()==False:
        step()
        paint()
    b+=1
if a=="W" and b==0:
    right()
    while is_wall()==False:
        step()
    right()
    while is_wall()==False:
        step()
        paint()
right()
while is_wall()==False:
   step()
paint()
right()
while is_wall()==False:
   step()
paint()
right()
while is_wall()==False:
   step()
paint()
