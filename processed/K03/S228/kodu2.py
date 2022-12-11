from pykkar import *

create_world("""
###############
#             #
#             #
#             #
#  v          #
#             #
###############
""")

while not is_wall():
    step()
right()
for i in range(4): #käsu leidsin videost https://youtu.be/S21p1EwNgA8?t=200 kui õppisime joonistama kilpkonnaga
    while not is_wall():
        step()
    paint()
    right()
