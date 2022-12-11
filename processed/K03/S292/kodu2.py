from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
########
#      #
#      #
#   <  #
#      #
#      #
########
""")

if get_direction() == E:
    right()
if get_direction() == N:
    right()
    right()
if get_direction() == W:
    right()
    right()
    right()
# liigu seinani
while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
    
if is_wall():
    right()

while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()  
paint()
right()
while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
paint()
right()
while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
paint()
right()
while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
paint()
right()