from pykkar import*

create_world("""
#########
#>      #
#       #
#       #
#       #
#       #
#########
""")

samme_jäänud = 24
while samme_jäänud > 0:
    if is_wall():
        paint()
        right()
    else:
        step()
        samme_jäänud -= 1