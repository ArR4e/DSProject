from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
##############
#            #
#            #
#            #
#            #
#           >#
##############
""")


while not is_wall():
    step()

right()


while not is_wall():
    step()

right()
paint()

while not is_wall():
    step()

right()
paint()

while not is_wall():
    step()

right()
paint()

while not is_wall():
    step()

right()
paint()
right()


# liigu seinani
"""loendur=0
i=0
while loendur <= 2:
    while not is_wall():
        step()
    while i <= 2:
        if is_wall():
            loendur+=1
            right()
            i+=1
        else:
           right()
           i+=1
    step()
print(loendur)"""

"""if not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    right()
elif not is_wall():
    right()
elif not is_wall():
    right()
else:
    while not is_wall():
        step()"""

# pööra ringi
