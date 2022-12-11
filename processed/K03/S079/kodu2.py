# 2. Pykkar igas maailma nurgas
# Kirjuta Pykkari programm, mis suvalise ristkülikukujulise maailma puhul värvib ära maailma iga nurga.
# Programm peab töötama olenemata roboti algpositsioonist ja vaatesuunast.
# Võib eeldada, et maailm on seest tühi (s.t pykkar asub ristkülikukujulises seest tühjas seintega piiratud maailmas).

# Automaatkontroll sellel ülesandel puudub, aga Moodle'isse tuleks lahendus esitada ikka.

from pykkar import *

create_world("""
##############
#            #
#       <    #
#            #
##############
    
""")

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
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()