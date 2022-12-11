from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
#############
#           #
#           #
#      >    #
#           #
#           #
#############
""")
def sein():
    #kui näeb seina teeb 360 kraadise pöörde
    #ja selle põhjal kas ta näeb kahte seina poolt/ ehk on nurgas, värvib
    x = 0
    if(is_wall()):
        x += 1
    right()
    if(is_wall()):
        x += 1
    right()
    if(is_wall()):
        x += 1
    right()
    if(is_wall()):
        x += 1
    right()
    if (x==2):
        paint()
        x = 0
while not is_painted():
    while(is_wall()):
        sein()
        right()
    while not is_wall(): 
        step()
