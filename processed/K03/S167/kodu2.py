from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
#########
#       #
#       #
#       #
#       #
#  ^    #
#########
""")

a = get_direction()
print(a)
while not is_wall():
     step()
     if is_wall():
         break
right()
while not is_wall():
     step()
     if is_wall():
         break
right()
paint()
while not is_wall():
     step()
     if is_wall():
         break
right()
paint()
while not is_wall():
     step()
     if is_wall():
         break
right()
paint()
while not is_wall():
     step()
     if is_wall():
         break
right()
paint()