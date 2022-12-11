from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")

while not is_wall():
    step()
right()


for i in range(4):
    while not is_wall(): 
        step()
    paint()
    right()

