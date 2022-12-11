#küsija ja tekstinfo moddelleerija/kasutajaliite loomine

#küsib kasutajalt eesnime
#küsib kasutajalt perenime
#väljastab kasuatajanime, mis on loodud eesnime ja perenime liitmisel, kus tähed on läbivalt väikesed ja ees- ja perenime eraldajaks on punkt

a = input(print("Mis on sinu eesnimi?"))
b = input(print("Mis on sinu perekonnanimi?"))

print(str.lower(a) + "." + str.lower(b))
#sõnede (peafunktsioon) puhul saab kasutada !liitfunktsiooni (peafunktsioon.liitfunktsioon)
#"lower" liitfunktsioon võtab näiteks funktsiooni "str" ehk stringi tähed lowercasiks

#if loogika abil saab täpitähed muuta konditsioonile