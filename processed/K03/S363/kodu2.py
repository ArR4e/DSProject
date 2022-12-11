from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
#########
#       #
#       #
#       #
#   v   #
#       #
#########
""")

#pööra üles
suund = get_direction()

while get_direction() != "N":
    right()
       
while not is_wall():
    step()
    
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