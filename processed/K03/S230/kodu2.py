from pykkar import *
i=0

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit, tühik tähistab heledat põrandat.
# Noole suund (>, <, v või ^) tähistab roboti suunda.

create_world("""
########
#      #
#   >  #
#      #
#      #
#      #
########
""")

while not is_wall():
    step()
while i < 4:
    i+=1
    right()
    while not is_wall():
        step()
    paint()
exitonclick()
