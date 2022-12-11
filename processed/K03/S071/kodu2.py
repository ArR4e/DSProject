#Kirjuta Pykkari programm, mis suvalise ristkülikukujulise maailma puhul värvib ära maailma iga nurga.
#Programm peab töötama olenemata roboti algpositsioonist ja vaatesuunast.
#Võib eeldada, et maailm on seest tühi (s.t pykkar asub ristkülikukujulises seest tühjas seintega piiratud maailmas).

from pykkar import *

create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")

nurki = 0
while nurki <= 10:
    if is_wall():
        paint()
        right()
    else:
        while not is_wall():
            step()
    nurki += 1