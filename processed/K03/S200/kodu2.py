from pykkar import*

create_world( """
########
#>     #
#      #
#      #
#      #
#      #
########
""")

i = 0 # loendur

while i < 4:
    while not is_wall():
        step()
    paint()
    right()
    i += 1