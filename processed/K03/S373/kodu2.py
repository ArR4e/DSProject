from pykkar import*
create_world("""
########
#>     #
#      #
#      #
#      #
#      #
#      #
########
""")
kordus = 0
while kordus < 4:
    step()
    step()
    step()
    step()
    step()
    paint()
    right()
    kordus = kordus +1