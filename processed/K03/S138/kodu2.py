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

def Nurgas():
    i = 0
    kogus = 0
    while i < 4:
        i = i + 1
        if is_wall():
            kogus = kogus + 1
        right()
    return kogus

while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
värvitud = 0
while True:
    nurgas = Nurgas()
    if nurgas == 1:
        right()
        while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
            step()
    elif nurgas == 2:
        värvitud = värvitud + 1
        right()
        paint()
        if värvitud == 4:
            break
        while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
            step()
