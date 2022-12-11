#võtsin progeõpikust
from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
##########
#        #
#        #
#        #
# v      #
##########
""")

# liigu seinani
while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()

# pööra ringi
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
    
