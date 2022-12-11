from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
########
#  <   #
#      #
#      #
#      #
#      #
########
""")


asukoht = get_direction()

if asukoht == "S":
    right()
    right()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()

elif asukoht == "W":
    right()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    
elif asukoht == "N":
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    
elif asukoht == "E":
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()
    while not is_wall():
        step()
    paint()
    right()



