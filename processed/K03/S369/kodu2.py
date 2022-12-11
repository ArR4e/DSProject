from pykkar import *
 
# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
##################
# >              #
#                #
#                #
#                #
#                #
##################
""")

# otsib nurka
def bottom_right_corner_search():
    while not is_wall():
        step()
    right()
    step()
    while not is_wall():
        step()
    paint()
    right()

def next_corner():
    while not is_wall():
        step()
    paint()
    right()
    
bottom_right_corner_search()
next_corner()
next_corner()
next_corner()
