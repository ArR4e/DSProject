from pykkar import *
create_world("""
########
#      #
#     >#
#      #
#      #
#      #
########
""")
i = 1
while i > 0:
    if get_direction() != 'N': #eesmärgiks saada robot näoga põhja
        right()
    elif get_direction() == 'N':
        i -=1
        right()
while not is_wall(): #kui peaks kuskil keskel startima, siis läheb seina äärde
    step()   
right()
while not is_wall(): #seina äärest läheb lähimasse nurka ja hakkab liikua + värvima
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

