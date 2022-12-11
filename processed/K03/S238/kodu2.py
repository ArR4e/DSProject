from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
########
#      #
#      #
#  >   #
#      #
#      #
########
""")

# liigu seinani
while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
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

