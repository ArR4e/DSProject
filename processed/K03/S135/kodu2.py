from pykkar import *

# Kirjuta Pykkari programm, mis suvalise ristkülikukujulise
# maailma puhul värvib ära maailma iga nurga. 

nurkadeArv = 0

# loob maailma
create_world("""
#########
#       #
#       #
#       #
#   ^   #
#       #
#########
""")

# kõnnib kuni ees on sein ja siis keerab
while True:
    if is_wall():
        right()
        break
    step()
    
# kui ees on ikka sein, siis pykkar on nurgas ja teeb nurga ruudu tumedaks ja keerab
if is_wall():
    paint()
    right()
    nurkadeArv += 1

# pykkar peaks nüüd seina kõrval või nurgas olema.
# Liigub edasi kuni tuleb sein, värvib ruudu tumedaks ja keerab. Teeb seda kuni
# on käinud 4 nurgas 
while nurkadeArv != 4:
    if is_wall():
        paint()
        right()
        nurkadeArv += 1
    step()

