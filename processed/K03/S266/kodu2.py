# Pykkar igas maailma nurgas
from pykkar import*

create_world("""
#######
#     #
#     #
#     #
#v    #
#     #
#######
""")


while not is_wall():
    step()
right()

for i in range(4):
    while not is_wall():
        step()
    paint()
    right()                                                                                                                                                                                  