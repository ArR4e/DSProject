pikkus=int(input("Palun sisestage liini pikkus täisarvuna meetrites: "))
laius=int(input("Palun sisestage kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites: "))
#kuna min vahe saab täisarvude vahel olla 1, siis
postidearv=round(pikkus/laius)
hulk=pikkus/laius
ymeetrid=hulk-postidearv
#print(postidearv,hulk,ymeetrid)

if ymeetrid==0.0 or ymeetrid<0:
    postidearv=postidearv+1
if ymeetrid>0:
    postidearv=postidearv+2
if pikkus<laius:
    postidearv=2

print("Poste läheb vaja "+str(postidearv))