from pykkar import *
# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
#################
#               #
#         >     #
#               #
#################
""")
    
def gotowall():
    while not is_wall():
     step()

f = 0
g = get_direction()

gotowall()
right()
gotowall()
paint()
f += 1

while is_wall() and is_painted():
    right()
    gotowall()
    paint()
    f += 1
    if f == 4:
        break
