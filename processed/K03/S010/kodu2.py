from pykkar import *

create_world("""
#################
#               #
#               #
#        v      #
#               #
#               #
#               #
#################

""")                      # Ma ei tea, kas create_world() on selle ülesande puhul
                          # vajalik (kuna see peab töötama suvalise seest tühja 
                          # maailma korral), kuid ma igaks juhuks tegin koos sellega
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