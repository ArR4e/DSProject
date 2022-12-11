from math import *

#küsime kasutajalt sisendi.
pikkus = int(input("Sisestage liini pikkus: "));
postivahe = int(input("Sisestage liinil olevate postide maksimaalne vahe: "));

#jagame pikkuse maksimaalse postivahega, et saada postide arv,
#lisaks liidame 1 posti, mis on elektriliini viimane post.
var1 = ceil(pikkus / postivahe) + 1;

#juhul, kui maksimaalne vahe on suurem elektriliini pikkusest
#saame me postide arvuks 1, kuid liinil on vähemalt 2 posti, seega
#sätime postide arvu siin kaheks.
if(var1 < 2):
    var1 = 2;

#Prindime vastuse.
print(var1)
