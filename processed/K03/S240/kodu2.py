from pykkar import * #ei oska macbooki pykkarit salvestada, pole aimu kuidas kood peaks seal töötama

create_world ("""
########
# >    #
#      #
#      #
#      #
########
""")

while not is_wall():
    step()
else:
    paint()
    right()
    

