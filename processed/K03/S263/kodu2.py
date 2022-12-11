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


if is_wall:
    right()
    step()

while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
# pööra ringi
right()

while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
# pööra ringi
right()
paint()

while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
# pööra ringi
right()
paint()

while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
# pööra ringi
right()
paint()

while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
# pööra ringi
right()
paint()
